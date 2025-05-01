import requests
import xml.etree.ElementTree as ET
import csv

# Input files
collections_file = "collections.txt"
csv_filename = "all_products.csv"

# Shopify-compatible headers
headers = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Product Category", "Type", "Tags", "Published",
    "Option1 Name", "Option1 Value", "Option1 Linked To", "Option2 Name", "Option2 Value",
    "Option2 Linked To", "Option3 Name", "Option3 Value", "Option3 Linked To", "Variant SKU",
    "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Policy",
    "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price",
    "Variant Requires Shipping", "Variant Taxable", "Variant Barcode", "Image Src",
    "Image Position", "Image Alt Text", "Gift Card", "SEO Title", "SEO Description",
    "Google Shopping / Google Product Category", "Google Shopping / Gender",
    "Google Shopping / Age Group", "Google Shopping / MPN", "Google Shopping / Condition",
    "Google Shopping / Custom Product", "Google Shopping / Custom Label 0",
    "Google Shopping / Custom Label 1", "Google Shopping / Custom Label 2",
    "Google Shopping / Custom Label 3", "Google Shopping / Custom Label 4",
    "Google: Custom Product (product.metafields.mm-google-shopping.custom_product)",
    "Product rating count (product.metafields.reviews.rating_count)",
    "Age group (product.metafields.shopify.age-group)",
    "Clothing features (product.metafields.shopify.clothing-features)",
    "Color (product.metafields.shopify.color-pattern)",
    "Dress occasion (product.metafields.shopify.dress-occasion)",
    "Dress style (product.metafields.shopify.dress-style)",
    "Fabric (product.metafields.shopify.fabric)",
    "Neckline (product.metafields.shopify.neckline)",
    "Scarf/Shawl style (product.metafields.shopify.scarf-shawl-style)",
    "Size (product.metafields.shopify.size)",
    "Skirt/Dress length type (product.metafields.shopify.skirt-dress-length-type)",
    "Sleeve length type (product.metafields.shopify.sleeve-length-type)",
    "Target gender (product.metafields.shopify.target-gender)",
    "Complementary products (product.metafields.shopify--discovery--product_recommendation.complementary_products)",
    "Related products (product.metafields.shopify--discovery--product_recommendation.related_products)",
    "Related products settings (product.metafields.shopify--discovery--product_recommendation.related_products_display)",
    "Search product boosts (product.metafields.shopify--discovery--product_search_boost.queries)",
    "Variant Image", "Variant Weight Unit", "Variant Tax Code", "Cost per item",
    "Included / India", "Price / India", "Compare At Price / India", "Status"
]

def extract_text(xml, tag):
    el = xml.find(tag)
    return el.text.strip() if el is not None and el.text else ''

# Read collection URLs from file
with open(collections_file, 'r') as f:
    collection_urls = [line.strip() for line in f if line.strip()]

# Start processing
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()

    for url in collection_urls:
        if "?" in url:
            atom_url = url.replace("/collections/", "/collections/.atom")
        else:
            atom_url = url + ".atom"

        print(f"📡 Fetching atom feed: {atom_url}")

        try:
            atom_response = requests.get(atom_url)
            atom_response.raise_for_status()
            atom_root = ET.fromstring(atom_response.content)
            ns = {'atom': 'http://www.w3.org/2005/Atom'}

            product_links = atom_root.findall(".//atom:link[@rel='alternate']", namespaces=ns)
            xml_urls = [link.attrib['href'] + ".xml" for link in product_links if 'href' in link.attrib]

            print(f"🔗 Found {len(xml_urls)} product links")

            for xml_url in xml_urls:
                try:
                    print(f"⏳ Processing: {xml_url}")
                    product_response = requests.get(xml_url)
                    product_response.raise_for_status()
                    product_root = ET.fromstring(product_response.content)

                    handle = extract_text(product_root, 'handle')
                    title = extract_text(product_root, 'title')
                    body_html = extract_text(product_root, 'body-html')
                    vendor = extract_text(product_root, 'vendor')
                    product_type = extract_text(product_root, 'product-type')
                    tags = extract_text(product_root, 'tags')
                    sku = extract_text(product_root, 'sku')
                    price = extract_text(product_root, 'price')
                    compare_at_price = extract_text(product_root, 'compare-at-price')

                    images = product_root.findall('.//image')
                    for image in images:
                        src_el = image.find('src')
                        pos_el = image.find('position')
                        if src_el is not None and pos_el is not None:
                            writer.writerow({
                                "Handle": handle,
                                "Title": title,
                                "Body (HTML)": body_html,
                                "Vendor": vendor,
                                "Type": product_type,
                                "Tags": tags,
                                "Variant SKU": sku,
                                "Variant Price": price,
                                "Variant Compare At Price": compare_at_price,
                                "Image Src": src_el.text.strip(),
                                "Image Position": pos_el.text.strip(),
                                "Published": "TRUE",
                                "Status": "active"
                            })

                    print(f"✅ Done: {handle}")
                except Exception as e:
                    print(f"❌ Error processing {xml_url}: {e}")

        except Exception as e:
            print(f"❌ Failed to fetch atom feed: {atom_url} — {e}")

print(f"\n🎉 All done! Output saved as {csv_filename}")
