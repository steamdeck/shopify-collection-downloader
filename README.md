<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Shopify Collection Scraper & Importer</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px;">

  <h1>🛍️ Shopify Collection Scraper & Importer</h1>
  <p>This Python script allows you to <strong>scrape products from any Shopify store's collection page</strong> and export them to a <code>CSV</code> file (<code>all_products.csv</code>) that can be directly imported into <strong>your own Shopify store</strong>.</p>

  <h2>📂 Project Structure</h2>
  <pre><code>shopify-scraper/
├── all_products.csv     # Output file with scraped product data
├── collections.txt      # Input file with one or more Shopify collection URLs
└── run.py               # Main Python script to run the scraper
</code></pre>

  <h2>🔧 How It Works</h2>
  <ol>
    <li>Add one or more Shopify collection URLs to <code>collections.txt</code>, one per line.</li>
    <li>Run the script:
      <pre><code>python run.py</code></pre>
    </li>
    <li>The script will:
      <ul>
        <li>Visit each collection URL</li>
        <li>Scrape all products (handling pagination)</li>
        <li>Save them to <code>all_products.csv</code></li>
      </ul>
    </li>
    <li>Upload <code>all_products.csv</code> to your own Shopify store via:
      <br><em>Shopify Admin → Products → Import</em>
    </li>
  </ol>

  <h2>✅ Supported Features</h2>
  <ul>
    <li>🔄 Handles multiple collections</li>
    <li>📦 Collects product title, description, price, images, and more</li>
    <li>📁 Outputs in Shopify-compatible CSV format</li>
    <li>🔁 Supports pagination for large collections</li>
  </ul>

  <h2>📥 Input Format (<code>collections.txt</code>)</h2>
  <p>Each line should be a <strong>Shopify collection URL</strong>, for example:</p>
  <pre><code>https://examplestore.myshopify.com/collections/sale
https://anotherstore.com/collections/all-products
</code></pre>

  <h2>🛒 Uploading to Your Store</h2>
  <ol>
    <li>Log in to your Shopify Admin.</li>
    <li>Navigate to <strong>Products &gt; Import</strong>.</li>
    <li>Click <strong>Add file</strong>, upload <code>all_products.csv</code>.</li>
    <li>Click <strong>Upload and continue</strong>.</li>
  </ol>

  <h2>🚀 Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li><code>requests</code>, <code>beautifulsoup4</code>, <code>csv</code>, <code>pandas</code> (if used)</li>
  </ul>
  <p>Install dependencies:</p>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h2>🧠 Notes</h2>
  <ul>
    <li>This tool assumes the target Shopify stores are public and don't block scrapers.</li>
    <li>Use responsibly and ensure you are complying with Shopify's and the store's Terms of Service.</li>
  </ul>

  <h2>📄 License</h2>
  <p>MIT License – Free to use and modify.</p>

</body>
</html>
