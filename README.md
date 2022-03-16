# EDA_Wish_Ecommerce

**Background**

**Wish** is operated by ContextLogic Inc. in [San Francisco](https://en.wikipedia.org/wiki/San_Francisco), United States. The platform employs browsing technologies that personalize shopping visually for each customer, rather than relying on a search bar format. It allows sellers to list their products on Wish and sell directly to consumers. Wish works with payment service providers to handle payments and does not stock the products themselves or manage returns.

**Wish** is an American online [e-commerce](https://en.wikipedia.org/wiki/E-commerce) platform that facilitates transactions between sellers and buyers. Wish was founded in 2010 by [Piotr Szulczewski](https://en.wikipedia.org/wiki/Piotr_Szulczewski) (CEO) and Danny Zhang (former CTO).


**Dataset Information**
- **About data**
    - The data comes from the Wish platform, an e-commerce site that is famous for selling items at affordable prices. This dataset contains product listings as well as products **ratings** and **sales performance.**
    - The data was scraped in the ***french localisation*** (hence some non-ascii Latin characters such as « é » and « à ») in the title column.
    - 
- **Columns information**
    
    There are 44 columns in the dataset:
    
    1. `**title_orig**`: contains the original title (the base title) that is displayed by default
    2. `**price`:** the price you would pay to get the product 
    3. `**retail_price`:** retail price, or reference price in other stores/places. Used by the seller to indicate a regular value or the price before discount
    4. `**retail_price_currency` :** discount price in currency
    5. `**discount_price`:** discount price
    6. `**discount_currency`:** currency of discount
    7. `**currency_buyer`:** currency of the prices
    8. `**units_sold`:** number of units sold. Lower bound approximation by steps
    9. `**uses_ad_boost`:** whether the seller paid to boost his product within the platform (highlighting, better placement, or whatever).
    10. `**rating`:** mean product rating
    11. `**rating_count`:** total number of ratings of the product
    12. `**rating_five_count` :** number of 5-star ratings 
    13. `**rating_four_count` :** number of 4-star ratings 
    14. `**rating_three_count` :** number of 3-star ratings 
    15. `**rating_two_count` :** number of 2-star ratings 
    16. `**rating_one_count` :** number of 1-star ratings 
    17. `**badges_count`:** number of badges the product or the seller has
    18. `**badges_local_product`:** a badge that denotes the product is a local product. Conditions may vary (being produced locally, or something else). Some people may prefer buying local products rather than. 1 means Yes, has the badge.
    19. `**badges_product_quality`:** badge awarded when many buyers consistently gave good evaluations 1 means Yes, has the badge
    20. `**badges_fast_shipping`:** badge awarded when this product's order is consistently shipped rapidly
    21. `**tags`:** tags set by the seller
    22. `**product_color`:** product's main color
    23. `**product_variation_size_id`:** one of the available size variations for this product
    24. `**product_variation_inventory`:** inventory the seller has. Max allowed quantity is 50
    25. `**shipping_option_name`:** type of shipping *(Livraison standard,Standard Shipping,...)*
    26. `**shipping_option_price`:** shipping price
    27. `**shipping_is_express`:** whether the shipping is express or not. 1 for True
    28. `**countries_shipped_to`:** number of countries this product is shipped to. Sellers may choose to limit where they ship a product to
    29. `**inventory_total**`: total inventory for all the product's variations (size/color variations for instance)
    30. `**has_urgency_banner**`: total inventory for all the product's variations (size/color variations for instance)
    31. `**urgency_text**`: a text banner that appears over some products in the search results.
    32. `**origin_country**`: seller location
    33. `**merchant_title**`: merchant's displayed name (show in the UI as the seller's shop name)
    34. `**merchant_name**`: merchant's canonical name. A name not shown publicly. Used by the website under the hood as a canonical name. Easier to process since all lowercase without white space
    35. `**merchant_info_subtitle**`: the subtitle text as shown on a seller's info section to the user. (raw, not preprocessed). The website shows this to the user to give an overview of the seller's stats to the user. Mostly consists of `% <positive_feedbacks> (<rating_count> reviews)` written in French
    36. `**merchant_rating_sell**`: number of ratings of this seller
    37. `**merchant_id**`: merchant unique id
    38. `**merchant_has_profile_picture**`: convenience boolean that says whether there is a `merchant_profile_picture` URL
    39. `**merchant_profile_picture**`: custom profile picture of the seller (if the seller has one). Empty otherwise.
    40. `**product_url**`: URL to the product page. You may need to log in to access it
    41. `**product_picture`:** URL
    42. `**product_id**`: product identifier. You can use this key to remove duplicate entries if you're not interested in studying them.
    43. `**theme**`: the search term used in the search bar of the website to get these search results.
    44. `**crawl_month:**` for info only


**Data source**
https://www.kaggle.com/jmmvutu/summer-products-and-sales-in-ecommerce-wish
