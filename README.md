# **BACKGROUND**

**Wish** is operated by ContextLogic Inc. in [San Francisco](https://en.wikipedia.org/wiki/San_Francisco), United States. The platform employs browsing technologies that personalize shopping visually for each customer, rather than relying on a search bar format. It allows sellers to list their products on Wish and sell directly to consumers. Wish works with payment service providers to handle payments and does not stock the products themselves or manage returns.

**Wish** is an American online [e-commerce](https://en.wikipedia.org/wiki/E-commerce) platform that facilitates transactions between sellers and buyers. Wish was founded in 2010 by [Piotr Szulczewski](https://en.wikipedia.org/wiki/Piotr_Szulczewski) (CEO) and Danny Zhang (former CTO).


# **Dataset Information**

- **About data**
    - The data comes from the Wish platform, an e-commerce site that is famous for selling items at affordable prices. This dataset contains product listings as well as products **ratings** and **sales performance.**
    - The data was scraped in the ***french localisation*** (hence some non-ascii Latin characters such as « é » and « à ») in the title column.
    
- **Columns information**
    
    There are 44 columns in the dataset:
    
    - `**title_orig**`: contains the original title (the base title) that is displayed by default
    - `**price`:** the price you would pay to get the product 
    - `**retail_price`:** retail price, or reference price in other stores/places. Used by the seller to indicate a regular value or the price before discount
    - `**retail_price_currency` :** discount price in currency
    - `**discount_price`:** discount price
    - `**discount_currency`:** currency of discount
    - `**currency_buyer`:** currency of the prices
    - `**units_sold`:** number of units sold. Lower bound approximation by steps
    - `**uses_ad_boost`:** whether the seller paid to boost his product within the platform (highlighting, better placement, or whatever).
    - `**rating`:** mean product rating
    - `**rating_count`:** total number of ratings of the product
    - `**rating_five_count` :** number of 5-star ratings 
    - `**rating_four_count` :** number of 4-star ratings 
    - `**rating_three_count` :** number of 3-star ratings 
    - `**rating_two_count` :** number of 2-star ratings 
    - `**rating_one_count` :** number of 1-star ratings 
    - `**badges_count`:** number of badges the product or the seller has
    - `**badges_local_product`:** a badge that denotes the product is a local product. Conditions may vary (being produced locally, or something else). Some people may prefer buying local products rather than. 1 means Yes, has the badge.
    - `**badges_product_quality`:** badge awarded when many buyers consistently gave good evaluations 1 means Yes, has the badge
    - `**badges_fast_shipping`:** badge awarded when this product's order is consistently shipped rapidly
    - `**tags`:** tags set by the seller
    - `**product_color`:** product's main color
    - `**product_variation_size_id`:** one of the available size variations for this product
    - `**product_variation_inventory`:** inventory the seller has. Max allowed quantity is 50
    - `**shipping_option_name`:** type of shipping *(Livraison standard,Standard Shipping,...)*
    - `**shipping_option_price`:** shipping price
    - `**shipping_is_express`:** whether the shipping is express or not. 1 for True
    - `**countries_shipped_to`:** number of countries this product is shipped to. Sellers may choose to limit where they ship a product to
    - `**inventory_total**`: total inventory for all the product's variations (size/color variations for instance)
    - `**has_urgency_banner**`: total inventory for all the product's variations (size/color variations for instance)
    - `**urgency_text**`: a text banner that appears over some products in the search results.
    - `**origin_country**`: seller location
    - `**merchant_title**`: merchant's displayed name (show in the UI as the seller's shop name)
    - `**merchant_name**`: merchant's canonical name. A name not shown publicly. Used by the website under the hood as a canonical name. Easier to process since all lowercase without white space
    - `**merchant_info_subtitle**`: the subtitle text as shown on a seller's info section to the user. (raw, not preprocessed). The website shows this to the user to give an overview of the seller's stats to the user. Mostly consists of `% <positive_feedbacks> (<rating_count> reviews)` written in French
    - `**merchant_rating_sell**`: number of ratings of this seller
    - `**merchant_id**`: merchant unique id
    - `**merchant_has_profile_picture**`: convenience boolean that says whether there is a `merchant_profile_picture` URL
    - `**merchant_profile_picture**`: custom profile picture of the seller (if the seller has one). Empty otherwise.
    - `**product_url**`: URL to the product page. You may need to log in to access it
    - `**product_picture`:** URL
    - `**product_id**`: product identifier. You can use this key to remove duplicate entries if you're not interested in studying them.
    - `**theme**`: the search term used in the search bar of the website to get these search results.
    - `**crawl_month:**` for info only


# **Data source**
https://www.kaggle.com/jmmvutu/summer-products-and-sales-in-ecommerce-wish

## **Define problems**

- **Problem Statement**
    
    Increasing penetration of the internet is bolstering the smartphone using population across the world. Digital content, travel and leisure, financial services, e-tailing among others constitute a variety of e-commerce options available to the internet accessing customer base that are gaining momentum with increased internet usage.
    
    This shows that e-commerce is a potential market for many retailers around the world.
    
    By offering their customers a way to browse specific items recommended to them, and focusing more on discounted pricing than anything else, Wish is turning eCommerce conventional wisdom on its head.
    
    **Some FAQ about Wish:**

- There are **over** **300 million items** available on Wish ([Indigo Digital](https://www.indigo9digital.com/blog/seven-things-you-may-not-know-about-wish-the-shopping-app-that-is-taking-on-ebay-and-amazon))
- A **third** of Wish’s total **order volume** comes from **the US** ([Forbes](https://www.forbes.com/sites/laurendebter/2020/07/30/wish-ecommerce-shipping-rate-increase-china-brick-and-mortar-stores-partnership/#7dbea53a4d6e))
- It is the **fourth** largest **online marketplace** in the **US** by sales volume
- Wish was the **most downloaded** shopping app in the world in **2018** ([Forbes](https://www.forbes.com/sites/parmyolson/2019/03/13/meet-the-billionaire-who-defied-amazon-and-built-wish-the-worlds-most-downloaded-e-commerce-app/#49154bd870f5))
- Wish **sells** about **three million items** daily
- Wish main demographic is **young and middle class** ([Cnet](https://www.cnet.com/news/shopping-app-wish-is-building-a-retail-empire-on-2-sunglasses/))

# **Solution Statement**
    
    To be more specific, the solution statement is to create a machine learning model that can forecast the sale volume of the merchant in Wish e-commerce by the classification algorithm, which has 7 classes followed in order by 100, 1.000, 5.000, 10.000, 20.000, 50.000, 100.000.
    
    Before that, we will explore data and answer a few questions to know deeply about this dataset.
    
    <aside>
    🕡 **A** **BIG QUESTION**: **What are the elements that help the new seller increase their sales?**
    
    </aside>
    
    - What is the difference between the 'price' from 'retail price' and how is the effect of the units sold?
    - Does having ad boosts increase success?
    - Is there any correlation between units sold and ratings?
    - Does a badge contribute to the sales of a product? What is the effect of different types of badges?
    - Do increased variations lead to increased success?
    - How does shipping affect sales?
    - Which tags should merchants use?
    - Does seller location affect sales?
    - What kind of merchants is likely to gain product success?
    - Do all product contains pictures?
    - What about the details of the merchant? Does not having a profile picture reduce success? Perhaps detailed info leads to higher success?
