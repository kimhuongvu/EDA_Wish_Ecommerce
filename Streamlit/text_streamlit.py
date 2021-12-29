home = '''
    # About Wish
    
    **Wish** is operated by ContextLogic Inc. in [San Francisco](https://en.wikipedia.org/wiki/San_Francisco), United States. 
    The platform employs browsing technologies that personalize shopping visually for each customer, rather than relying on a search bar format. 
    It allows sellers to list their products on Wish and sell directly to consumers. 
    Wish works with payment service providers to handle payments and does not stock the products themselves or manage returns.
    
    **Wish** is an American online [e-commerce](https://en.wikipedia.org/wiki/E-commerce) platform that facilitates transactions between sellers and buyers.
    Wish was founded in 2010 by [Piotr Szulczewski](https://en.wikipedia.org/wiki/Piotr_Szulczewski) (CEO) and Danny Zhang (former CTO). Wish** has become one of the most popular ecommerce platforms in the world — by selling an avalanche of cheap junky stuff, nearly all of it sourced from China. 
    Most of Wish’s customers are working-class people who can’t afford Amazon Prime and are more likely to shop at dollar stores. Today, just 20% of the company’s customers fork over $119 a year for Amazon Prime, while nearly 90% frequent Walmart.

    Some FAQ about Wish:

    - There are **over** **300 million items** available on Wish ([Indigo Digital](https://www.indigo9digital.com/blog/seven-things-you-may-not-know-about-wish-the-shopping-app-that-is-taking-on-ebay-and-amazon))
    - A **third** of Wish’s total **order volume** comes from **the US** ([Forbes](https://www.forbes.com/sites/laurendebter/2020/07/30/wish-ecommerce-shipping-rate-increase-china-brick-and-mortar-stores-partnership/#7dbea53a4d6e))
    - It is the **fourth** largest **online marketplace** in the **US** by sales volume
    - Wish was the **most downloaded** shopping app in the world in **2018** ([Forbes](https://www.forbes.com/sites/parmyolson/2019/03/13/meet-the-billionaire-who-defied-amazon-and-built-wish-the-worlds-most-downloaded-e-commerce-app/#49154bd870f5))
    - Wish **sells** about **three million items** daily
    - Wish main demographic is **young and middle class** ([Cnet](https://www.cnet.com/news/shopping-app-wish-is-building-a-retail-empire-on-2-sunglasses/))
    
    ## Problem Statement

    Increasing penetration of the internet is bolstering the smartphone using population across the world. Digital content, travel and leisure, financial services, e-tailing among others constitute a variety of e-commerce options available to the internet accessing customer base that are gaining momentum with increased internet usage.
    This shows that e-commerce is a potential market for many retailers around the world.
    By offering their customers a way to browse specific items recommended to them, and focusing more on discounted pricing than anything else, Wish is turning eCommerce conventional wisdom on its head.

    ## Solution Statement
    
    To be more specific, the solution statement is to create a machine learning model that can forecast the sale volume of the merchant in Wish e-commerce by the classification algorithm, which has 7 classes followed in order by 100, 1.000, 5.000, 10.000, 20.000, 50.000, 100.000.
    Before that, we will explore data and answer a few questions to know deeply about this dataset.
    
    **A** **BIG** **QUESTION**: What are the elements that help the new seller increase their sales?

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
    '''

dataset_info = '''
    - The data comes from the Wish platform, an e-commerce site that is famous for selling items at affordable prices. This dataset contains product listings as well as products **ratings** and **sales performance.**
    - The data was scraped in the ***french localisation*** (hence some non-ascii Latin characters such as « é » and « à ») in the title column.

    '''

columns_information = '''

    | Column name    		        | Description    	                                                            	                                                          
    |---					        |---				                                                                                                                      |
    | Title_orig       	            | contains the original title (the base title) that is displayed by default	                                                              |
    | Discount_price		        |  discount price                        			                                                                                      |  
    | Retail_price		            | retail price, or reference price in other stores/places.Used by the seller to indicate a regular value or the price before discount     |
    | Nb_cart_orders_approx         | number of units sold. Lower bound approximation by steps			                                                                      |
    | Rating	                    | mean product rating                                                   	                                                              |     
    | Product_color		            | product's main color                                           			                                                              |
    | Product_variation_size_id     | one of the available size variations for this product        				                                                              |
    | Product_variation_inventory	| inventory the seller has. Max allowed quantity is 50				                                                                      |
    | Shipping_option_price         | shipping price                                                                                                                          |
    | Merchant_title                | merchant's displayed name (show in the UI as the seller's shop name)                                                                    |                                               
    | Merchant_name                 | merchant's canonical name. A name not shown publicly. Used by the website under the hood as a canonical name. Easier to process since all lowercase without white space |
    <p><br></p>
    ---
    '''

data_source = '''
    --- 
    ## Data source: 

    Sales of summer clothes in E-commerce Wish   
    https://www.kaggle.com/jmmvutu/summer-products-and-sales-in-ecommerce-wish
    '''