from decimal import Decimal
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import (
    Category, Product,
    HeroImage, SmallBanner, Promotion,
    GalleryImage, Video
)

STATUS = "published"


class Command(BaseCommand):
    help = "Seed demo data: categories, products, hero, banners, promotions, gallery, videos."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete existing data before seeding.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        reset = options["reset"]

        if reset:
            Product.objects.all().delete()
            Category.objects.all().delete()
            HeroImage.objects.all().delete()
            SmallBanner.objects.all().delete()
            Promotion.objects.all().delete()
            GalleryImage.objects.all().delete()
            Video.objects.all().delete()

        # --- Reliable image URLs (Unsplash direct) ---
        IMG = {
            "shawarma": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "falafel_wrap": "https://images.unsplash.com/photo-1681072530653-db8fe2538631?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "baklava_1": "https://images.unsplash.com/photo-1658413380634-e127bbaeeb7b?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "baklava_2": "https://images.unsplash.com/photo-1676014959543-81df1079b423?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "kebab_plate": "https://images.unsplash.com/photo-1603360946369-dc9bb6258143?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "kebab_grill": "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "coffee_pot": "https://images.unsplash.com/photo-1732020486265-8757a4999d27?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "coffee_cup": "https://images.unsplash.com/photo-1695593217066-1e663f8524db?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "hummus": "https://images.unsplash.com/photo-1625943744308-2dce776f50e2?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "lemonade": "https://images.unsplash.com/photo-1566680011101-77f01de031d1?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "interior": "https://images.unsplash.com/photo-1646551479178-0c55c940a6b9?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
            "kunafa": "https://images.unsplash.com/photo-1741424605439-9b3b0f54d755?fm=jpg&ixlib=rb-4.1.0&q=80&w=1600",
        }

        # --- 5 Categories (Arabic restaurant) ---
        categories_data = [
            {
                "name_ar": "مشاوي",
                "name_en": "Grills",
                "name_ms": "Panggang",
                "image_url": IMG["kebab_grill"],
            },
            {
                "name_ar": "مقبلات",
                "name_en": "Appetizers",
                "name_ms": "Pembuka Selera",
                "image_url": IMG["hummus"],
            },
            {
                "name_ar": "سندويشات",
                "name_en": "Sandwiches",
                "name_ms": "Sandwic",
                "image_url": IMG["shawarma"],
            },
            {
                "name_ar": "حلويات",
                "name_en": "Desserts",
                "name_ms": "Pencuci Mulut",
                "image_url": IMG["baklava_1"],
            },
            {
                "name_ar": "مشروبات",
                "name_en": "Drinks",
                "name_ms": "Minuman",
                "image_url": IMG["lemonade"],
            },
        ]

        categories = {}
        for c in categories_data:
            obj, _ = Category.objects.get_or_create(
                name_ar=c["name_ar"],
                defaults={
                    "name_en": c["name_en"],
                    "name_ms": c["name_ms"],
                    "image_url": c["image_url"],
                    "status": STATUS,
                },
            )
            # لو موجود مسبقاً، نحدّثه (مفيد لو شغلت seed بدون reset)
            obj.name_en = c["name_en"]
            obj.name_ms = c["name_ms"]
            obj.image_url = c["image_url"]
            obj.status = STATUS
            obj.save()
            categories[c["name_ar"]] = obj

        # --- Products: 5-10 each category (هنا 7 لكل فئة = ضمن طلبك) ---
        products_by_category = {
            "مشاوي": [
                ("كباب لحم", "Beef Kebab", "Kebab Daging", "أسياخ كباب لحم مشوي مع خبز وصلصة.", "Grilled beef kebab skewers with bread & sauce.", "Kebab daging panggang dengan roti & sos.", "24.90", IMG["kebab_plate"], True),
                ("شيش طاووق", "Shish Tawook", "Shish Tawook", "دجاج متبل ومشوي مع ثوم.", "Marinated grilled chicken with garlic sauce.", "Ayam panggang perapan dengan sos bawang.", "21.90", IMG["kebab_grill"], False),
                ("مشاوي مشكلة", "Mixed Grill", "Panggang Campur", "تشكيلة مشاوي متنوعة.", "Assorted grilled meats.", "Aneka daging panggang.", "39.90", IMG["kebab_grill"], True),
                ("أوصال لحم", "Beef Tikka", "Tikka Daging", "قطع لحم مشوية مع بهارات.", "Spiced grilled beef cubes.", "Kiub daging panggang berempah.", "26.90", IMG["kebab_plate"], False),
                ("كفتة مشوية", "Grilled Kofta", "Kofta Panggang", "كفتة لحم مشوية مع بقدونس.", "Grilled kofta with parsley.", "Kofta panggang dengan daun parsli.", "22.90", IMG["kebab_plate"], False),
                ("صدر دجاج مشوي", "Grilled Chicken Breast", "Dada Ayam Panggang", "صدر دجاج مشوي خفيف.", "Light grilled chicken breast.", "Dada ayam panggang ringan.", "19.90", IMG["kebab_grill"], False),
                ("ريش غنم", "Lamb Chops", "Kotelet Kambing", "ريش غنم مشوية.", "Grilled lamb chops.", "Kotelet kambing panggang.", "44.90", IMG["kebab_grill"], True),
            ],
            "مقبلات": [
                ("حمص", "Hummus", "Hummus", "حمص بطحينة وزيت زيتون.", "Chickpea hummus with tahini & olive oil.", "Hummus dengan tahini & minyak zaitun.", "9.90", IMG["hummus"], True),
                ("متبل باذنجان", "Baba Ganoush", "Baba Ganoush", "باذنجان مشوي مع طحينة.", "Smoky eggplant dip with tahini.", "Celup terung dengan tahini.", "10.90", IMG["hummus"], False),
                ("تبولة", "Tabbouleh", "Tabbouleh", "سلطة بقدونس وبرغل.", "Parsley & bulgur salad.", "Salad parsli & bulgur.", "11.90", IMG["hummus"], False),
                ("فتوش", "Fattoush", "Fattoush", "سلطة خضار مع خبز محمص.", "Mixed salad with toasted bread.", "Salad campur dengan roti rangup.", "12.90", IMG["hummus"], False),
                ("بطاطا مقلية", "French Fries", "Kentang Goreng", "بطاطا مقرمشة.", "Crispy fries.", "Kentang goreng rangup.", "7.90", IMG["falafel_wrap"], False),
                ("ورق عنب", "Grape Leaves", "Daun Anggur", "ورق عنب محشي.", "Stuffed grape leaves.", "Daun anggur berinti.", "13.90", IMG["hummus"], False),
                ("مقبلات مشكلة", "Mixed Appetizers", "Pembuka Selera Campur", "تشكيلة من المقبلات.", "Assorted appetizers platter.", "Pinggan pembuka selera campur.", "29.90", IMG["hummus"], True),
            ],
            "سندويشات": [
                ("شاورما دجاج", "Chicken Shawarma", "Shawarma Ayam", "شاورما دجاج مع مخلل وثوم.", "Chicken shawarma with pickles & garlic.", "Shawarma ayam dengan jeruk & bawang.", "14.90", IMG["shawarma"], True),
                ("شاورما لحم", "Beef Shawarma", "Shawarma Daging", "شاورما لحم مع طحينة.", "Beef shawarma with tahini.", "Shawarma daging dengan tahini.", "16.90", IMG["shawarma"], False),
                ("فلافل", "Falafel Wrap", "Wrap Falafel", "فلافل مع خضار وطحينة.", "Falafel with veggies & tahini.", "Falafel dengan sayur & tahini.", "12.90", IMG["falafel_wrap"], True),
                ("كباب ساندويش", "Kebab Sandwich", "Sandwic Kebab", "كباب داخل خبز مع صوص.", "Kebab in bread with sauce.", "Kebab dalam roti dengan sos.", "17.90", IMG["kebab_plate"], False),
                ("صاج زعتر", "Zaatar Saj", "Saj Zaatar", "خبز صاج مع زعتر.", "Saj bread with zaatar.", "Roti saj dengan zaatar.", "9.90", IMG["shawarma"], False),
                ("صاج جبنة", "Cheese Saj", "Saj Keju", "خبز صاج مع جبنة.", "Saj bread with cheese.", "Roti saj dengan keju.", "10.90", IMG["shawarma"], False),
                ("ساندويش حلومي", "Halloumi Sandwich", "Sandwic Halloumi", "حلومي مشوي مع خضار.", "Grilled halloumi with veggies.", "Halloumi panggang dengan sayur.", "15.90", IMG["falafel_wrap"], False),
            ],
            "حلويات": [
                ("بقلاوة", "Baklava", "Baklava", "بقلاوة بالفستق.", "Pistachio baklava.", "Baklava pistachio.", "12.90", IMG["baklava_1"], True),
                ("كنافة", "Kunafa", "Kunafa", "كنافة ساخنة مع قطر.", "Hot kunafa with syrup.", "Kunafa panas dengan sirap.", "16.90", IMG["kunafa"], True),
                ("مهلبية", "Muhallebi", "Muhallebi", "مهلبية بالحليب.", "Milk pudding dessert.", "Puding susu.", "9.90", IMG["baklava_2"], False),
                ("رز بحليب", "Rice Pudding", "Puding Beras", "رز بحليب وقرفة.", "Rice pudding with cinnamon.", "Puding beras dengan kayu manis.", "9.90", IMG["baklava_2"], False),
                ("كيك تمر", "Date Cake", "Kek Kurma", "كيك تمر طري.", "Soft date cake.", "Kek kurma lembut.", "11.90", IMG["baklava_2"], False),
                ("تمر مع طحينة", "Dates & Tahini", "Kurma & Tahini", "تمر فاخر مع طحينة.", "Premium dates with tahini.", "Kurma premium dengan tahini.", "10.90", IMG["baklava_1"], False),
                ("حلا مشكل", "Dessert Mix", "Pencuci Mulut Campur", "تشكيلة حلويات.", "Assorted desserts.", "Aneka pencuci mulut.", "29.90", IMG["baklava_1"], True),
            ],
            "مشروبات": [
                ("ليمون بالنعناع", "Mint Lemonade", "Limau Pudina", "ليمون منعش بالنعناع.", "Refreshing mint lemonade.", "Limau pudina menyegarkan.", "8.90", IMG["lemonade"], True),
                ("قهوة عربية", "Arabic Coffee", "Kopi Arab", "قهوة عربية بالهيل.", "Arabic coffee with cardamom.", "Kopi Arab dengan buah pelaga.", "7.90", IMG["coffee_cup"], True),
                ("شاي مغربي", "Moroccan Tea", "Teh Maghribi", "شاي بالنعناع.", "Mint tea.", "Teh pudina.", "7.90", IMG["coffee_pot"], False),
                ("مياه", "Water", "Air", "مياه شرب.", "Drinking water.", "Air minuman.", "2.90", IMG["lemonade"], False),
                ("عصير برتقال", "Orange Juice", "Jus Oren", "عصير برتقال طبيعي.", "Fresh orange juice.", "Jus oren segar.", "9.90", IMG["lemonade"], False),
                ("آيس كوفي", "Iced Coffee", "Kopi Ais", "قهوة باردة.", "Iced coffee.", "Kopi ais.", "11.90", IMG["coffee_cup"], False),
                ("مشروب غازي", "Soft Drink", "Minuman Bergas", "بيبسي/كولا.", "Pepsi/Coke.", "Pepsi/Kola.", "4.90", IMG["lemonade"], False),
            ],
        }

        created_products = 0
        for cat_name_ar, items in products_by_category.items():
            cat = categories[cat_name_ar]
            for (
                name_ar, name_en, name_ms,
                desc_ar, desc_en, desc_ms,
                price, image_url, is_recommended
            ) in items:
                obj, created = Product.objects.get_or_create(
                    category=cat,
                    name_ar=name_ar,
                    defaults={
                        "name_en": name_en,
                        "name_ms": name_ms,
                        "description_ar": desc_ar,
                        "description_en": desc_en,
                        "description_ms": desc_ms,
                        "price": Decimal(price),
                        "image_url": image_url,
                        "is_recommended": is_recommended,
                        "status": STATUS,
                    }
                )
                if not created:
                    obj.name_en = name_en
                    obj.name_ms = name_ms
                    obj.description_ar = desc_ar
                    obj.description_en = desc_en
                    obj.description_ms = desc_ms
                    obj.price = Decimal(price)
                    obj.image_url = image_url
                    obj.is_recommended = is_recommended
                    obj.status = STATUS
                    obj.save()
                created_products += 1

        # --- HeroImage (3) ---
        hero_urls = [IMG["interior"], IMG["kebab_plate"], IMG["coffee_cup"]]
        for url in hero_urls[:3]:
            HeroImage.objects.get_or_create(image_url=url, defaults={"status": STATUS})

        # --- SmallBanner (4) ---
        banner_urls = [IMG["shawarma"], IMG["hummus"], IMG["lemonade"], IMG["baklava_2"]]
        for url in banner_urls[:4]:
            SmallBanner.objects.get_or_create(
                image_url=url,
                defaults={"link": "", "status": STATUS}
            )

        # --- Promotion (4) ---
        promo_urls = [IMG["kebab_grill"], IMG["kebab_plate"], IMG["baklava_1"], IMG["coffee_pot"]]
        for url in promo_urls[:4]:
            Promotion.objects.get_or_create(
                image_url=url,
                defaults={"link": "", "status": STATUS}
            )

        # --- GalleryImage (10) ---
        gallery_urls = [
            IMG["interior"], IMG["kebab_plate"], IMG["kebab_grill"], IMG["shawarma"],
            IMG["falafel_wrap"], IMG["hummus"], IMG["lemonade"], IMG["coffee_cup"],
            IMG["baklava_1"], IMG["kunafa"],
        ]
        for url in gallery_urls[:10]:
            GalleryImage.objects.get_or_create(image_url=url, defaults={"status": STATUS})

        # --- Video (5) ---
        video_urls = [
            "https://www.youtube.com/watch?v=TROZvPHqP1g",  # shawarma
            "https://www.youtube.com/watch?v=EsZFJEjANiA",  # hummus
            "https://www.youtube.com/watch?v=NZcWedPKysk",  # falafel
            "https://www.youtube.com/watch?v=09WqwH4aiHY",  # kunafa
            "https://www.youtube.com/watch?v=kfxX-79sVjQ",  # arabic coffee
        ]
        for url in video_urls[:5]:
            Video.objects.get_or_create(video_url=url, defaults={"status": STATUS})

        self.stdout.write(self.style.SUCCESS("✅ Demo data seeded successfully."))
        self.stdout.write(self.style.SUCCESS(f"Categories: {Category.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Products: {Product.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"HeroImage: {HeroImage.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"SmallBanner: {SmallBanner.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Promotion: {Promotion.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"GalleryImage: {GalleryImage.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Video: {Video.objects.count()}"))
