import asyncio
from collections import deque
from random import choice

from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from sbb_b import sbb_b 
from ..core.managers import edit_delete, edit_or_reply

samir4 = ["على إيش سهران ؟",
            "مين تتوقع يطالعك طول الوقت بدون ملل ؟",
            "وين جالس الحين ؟",
            "كم من عشرة تقيم يومك ؟",
            "أطول مدة نمت فيها كم ساعه ؟",
            "أجمل سنة ميلادية مرت عليك ؟",
            "أخر رسالة بالواتس جاتك من مين ؟",
            "ليه مانمت ؟",
            "تعتقد فيه أحد يراقبك ؟",
            "كم من عشره تعطي حظك ؟",
            "كلمه ماسكه معك الفترة هذي ؟",
            "شيء مستحيل تمل منه ؟",
            "متى تنام بالعادة ؟",
            "كم من عشرة جاهز للدراسة ؟",
            "منشن صديقك الفزعة",
            "يوم نفسك يرجع بكل تفاصيله ؟",
            "أجمل صورة بجوالك ؟",
            "ايش أغرب مكان قد صحتوا فيه؟",
            "اذا جاك خبر مفرح اول واحد تعلمه فيه مين ؟",
            "شيء لو يختفي تصير الحياة جميلة ؟",
            "كم من عشرة تشوف نفسك محظوظ ؟",
            "امدح نفسك بكلمة وحدة بس",
            "كلمة لأقرب شخص لقلبك ؟",
            "قوة الصداقة بالمدة ولا بالمواقف ؟",
            "تتابع مسلسلات ولا م تهتم ؟",
            "تاريخ يعني لك الكثير ؟",
            "كم عدد اللي معطيهم بلوك ؟",
            "من الغباء انك ؟",
            "اكثر شيء محتاجه الحين ؟",
            "ايش مسهرك ؟.",
            "حزين ولا مبسوط ؟",
            "تحب سوالف مين ؟",
            "كم من عشرة روتينك ممل ؟",
            "شيء مستحيل ترفضه ؟.",
            "كم من عشرة الإيجابية فيك ؟.",
            "تعتقد اشباهك الاربعين عايشين حياة حلوة ؟.",
            "مين جالس عندك ؟",
            "كم من عشرة تشوف نفسك انسان ناجح ؟",
            "شيء حظك فيه حلو ؟.",
            "كم من عشرة الصبر عندك ؟",
            "أخر مرة نزل عندكم مطر ؟",
            "اكثر مشاكلك بسبب ؟",
            "اكره شعور ممكن يحسه انسان ؟",
            "شخص تحب تنشبله ؟",
            "تنتظر شيء ؟",
            "جربت تسكن وحدك ؟",
            "اكثر لونين تحبهم مع بعض ؟",
            "متى تكره نفسك ؟",
            "كم من عشرة مروق ؟",
            "مدينة تتمنى تعيش وتستقر فيها طول عمرك ؟",
            "لو للحياة لون إيش بيكون لون حياتك ؟",
            "ممكن في يوم من الأيام تصبح شخص نباتي ؟.",
            "عمرك قابلت شخص يشبهك ؟",
            "اخر شخص تهاوشت معه ؟",
            "قبل ساعة ايش كنت تسوي ؟",
            "كلمة تقولها للي ببالك ؟",
            "أكثر شيء مضيع وقتك فيه ؟",
            "لو فتحتا خزانتك إيش اكثر لون بنشوف ؟",
            "قوة خارقة تتمنى تمتلكها ؟",
            "اكثر مصايبك مع مين ؟",
            "اذا زعلت إيش يرضيك ؟",
            "من النوع اللي تعترف بسرعه ولا تجحد ؟",
            "من الاشياء البسيطة اللي تسعدك ؟",
            "اخر مره بكيت",
            "ايموجي يعبر عن وضعك الحين ؟",
            "التاريخ المنتظر بالنسبة لك ؟",
            "كلنا بنسمعك إيش بتقول ؟",
            "مدينتك اللي ولدت فيها ؟",
            "عندك شخص مستحيل يمر يوم وما تكلمه ؟",
            "كلمة تقولها لنفسك ؟",
            "كم من عشرة متفائل بالمستقبل ؟",
            "ردك المعتاد اذا أحد ناداك ؟",
            "أكثر كلمه تسمعها من أمك ؟",
            "إيش تفضل عمل ميداني ولاعمل مكتبي ؟",
            "أكثر حيوان تحبه ؟",
            "اكثر مشاكلك بسبب ؟",
            "اكثر صوت تكرهه ؟",
            "اشياء تتمنى انها م تنتهي ؟",
            "اشياء صعب تتقبلها بسرعه ؟",
            "كم من عشرة راضي عن وضعك الحالي ؟",
            "متى م تقدر تمسك ضحكتك ؟",
            "اخر شخص قالك كلمة حلوة ؟",
            "اكثر شيء تحبه بنفسك ؟",
            "شيء نفسك يرجع ؟",
            "اغلب وقتك ضايع على ؟",
            "كيف تعرفت على اعز صديق لك ؟",
            "شايل هم شيء الفترة هذي ؟",
            "شخص م تحب تناقشه ؟",
            "تقييمك للديسكورد الفترة هذي ؟",
            "من النوع اللي اذا حطيت راسك على المخده نمت ولا تحتاج وقت ",
            "اهم برنامج عندك بالجوال الفترة هذي ؟",
            "كم تعطي نفسك من عشرة بتعاملك مع مشاكلك ؟",
            "اشياء تبين عليك اذا زعلت ؟",
            "كم من عشرة تحب الجلسة بالبيت ؟",
            "أطول مكالمة لك كم كانت مدتها ؟",
            "اسم تحس صاحبه فخم ؟",
            "تتكلم أكثر ولا تسمع ؟",
            "كم من عشرة تحب النوم ؟",
            "اخر شيء اكلته ؟",
            "أكثر مكان سافرت له بخيالك ؟",
            "كبرت وللحين اخاف من ؟",
            "كيف حالك وانت لحالك ؟",
            "أكثر اسم تحبه ؟.",
            "اكبر مبلغ ضاع منك ؟",
            "كلمة تختصر وضعك الحين ؟",
            "نظام نومك ...",
            "أكثر مكان تجلس فيه غير غرفتك ؟",
            "حرف تحبه ؟",
            "كم درجة الحرارة بمدينتك ؟",
            "تعطي اللي غلط بحقك فرصة ؟",
            "حياتك بكلمة ؟",
            "عندك مليون ريال بس مايمديك تشتري الا شيء  يبدأ بأول حرف من اسمك. وش بتشتري ؟",
            "اكثر شيء ساحب عليه الفترة هذي ؟",
            "شيء مستحيل تعطيه أحد ؟",
            "تنتظر شيء ؟",
            "ايش الوظيفة التي تستحق أعلى راتب؟",
            "كم مره تشحن جوالك باليوم ؟",
            "كم من عشرة عندك امل انك تصير مليونير ؟",
            "اشياء م تسويها غير اذا كنت مروق ؟",
            "لو بيدك تغير بالزمن, تقدمه ولا ترجعه ؟.",
            "دولة امنيتك تزورها ؟.",
            "اكثر  شخص فاهمك بالدنيا ؟",
            "تسامح بسرعة ؟.",
            "كم تحتاج وقت عشان تتعود على مكان جديد ؟",
            "كم من عشرة تحب الهدوء ؟",
            "تاريخ مهم جداً عندك ؟",
            "لعبة تشوف نفسك فنان فيها ؟",
            "أصعب قرار ممكن تتخذه ؟",
            "شيء نفسك تجربه ؟",
            "أشياء توترك ؟",
            "كم من عشرة تحب الاطفال ؟.",
            "اكثر شخص تتهاوش معه ؟",
            "لو خيروك بين يعطونك مليون أو راتب شهري متوسط بدون عمل مدى الحياة إيش تختار ؟",
            "الفلوس كل شيء ؟",
            "عشان تعيش مرتاح ؟",
            "ردة فعلك لو شفت شخص يبكي قدامك ؟",
            "كم مره أخذت عمره بـ رمضان ؟",
            "ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "شيء تشوف نفسك مبدع فيه ؟",
            "ماذا تفعل الان ؟ ",
            "كم من عشرة تحب حياتك ؟.",
            "كم عدد الصور بجوالك ؟.",
            "كم عدد اصحابك المقربين منك كثير ؟.",
            "شكراً لأنك في حياتي ..تقولها لمين ؟",
            "كيف تتعامل مع الشخص اللي يرد متأخر دائماً ؟.",
            "اللوان داكنة  ولا فاتحه؟",
            "كيف تتعامل مع الاشخاص السلبيين ؟",
            "دايم الانطباع الاول عنك إنك شخص ؟",
            "شيء حلو صار لك اليوم ؟",
            "اول شيء يلفت انتباهك بشخص اول مرة تقابله ؟.",
            "جماد م تستغني عنه ؟.",
            "مع ، ضد : البكاء يقلل التوتر ..!",
            "إيش كان نكك ايام البيبي ؟.",
            "من النوع اللي تحفظ اسامي الناس  بسرعه ولا بس اشكالهم ؟.",
            "لو كان لك الحرية تغير اسمك إيش راح تختار اسم ؟",
            "اكثر شيء ضيعت عليه فلوسك ؟",
            "تعرف تمسك نفسك اذا عصبت ؟",
            "عمرك شاركت بمسابقة وربحت ؟",
            "إيش لون جوالك ؟.",
            "تعتقد إنك انسان لك فايدة ؟",
            "اذا احد سألك عن شيء م تعرفه تقول م اعرف ولا تتفلسف ؟",
            "أطول صداقة بينك وبين شخص كم مدتها ؟.",
            "تعرف تعبر عن الكلام اللي بداخلك ؟",
            "ردة فعلك اذا انحشرت بالنقاش ؟",
            "بالعادة برمضان تنحف ولاتسمن ؟",
            "تمارس رياضة معينة برمضان ؟",
            "عندك فوبيا من شيء ؟.",
            "الساعة كم اذان الفجر عندكم ؟",
            "شيء من الماضي للحين عندك ؟.",
            "عندك شخص انت حييل جريء معاه و ما تستحي منه ؟",
            "عمرك انتقمت من شخص؟",
            "اكثر شي يتعبك بالصيام العطش ولا الجوع ؟",
            "اكثر شخص يتصل عليك بالواتس ؟",
            "متى اخر مره جربت شعور ليتني سكت بس ؟",
            "اسم ولد وبنت تحسهم لايقين على بعض ؟.",
            "مسلسل ناوي تشوفه ؟",
            "عادي تتغير عشان شخص تحبه ؟",
            "شيء كل م تذكرته تستانس؟",
            "ايامك هالفترة عبارة عن ؟",
            "منشن شخصين تحسهم نفس الاسلوب او الشخصية ..",
            "اكثر شيء بتشتاق له اذا جاء رمضان ؟",
            "كم مره سامحت بقلبك بس عقلك رافض هالشيء ؟.",
            "مع او ضد .. البنت تحب انشاء المشاكل في العلاقات ..",
            "ماهي طريقتك في معاتبة شخص ؟",
            "لو كنت محتار بين شخص تحبه وشخص يحبك، من تختار؟",
            "الشيء الي تحسه يجذبك للشخص هو ؟",
            "اكثر شخص بينك وبينه تواصل دائم ؟",
            "اعلى نسبة جبتها بحياتك الدراسية ؟",
            "شايل هم شيء ؟ ",
            "إيش تفضل صح وخطأ ولا خيارات ؟",
            "اكثر ايموجي تستخدمه ؟",
            "جربت ينسحب جوالك فترة الاختبارات ؟.",
            "مادة دايم تجيب العيد فيها ؟",
            "وجبة ساحب عليها ؟",
            "تحب تتعرف على ناس جدد ولا مكتفي باللي عندك ؟",
            "مادة تكرها بس درجاتك عالية فيها ؟",
            "شيء بسيط قادر يعدل مزاجك بشكل سريع ؟",
            "اطول مدة جلسة تذاكر فيها بشكل متواصل كم ساعة ؟",
            "قبل امس الوقت هذا إيش كنت تسوي ؟",
            "منشن شخص لو م شفته تحس يومك ناقص ؟",
            "كلمتك اذا شفت حاجة حلوة ؟",
            "خوالك ولا عمامك ؟",
            "عادي تطلع وجوالك مافيه شحن كثير ؟",
            "شيء من صغرك ماتغير فيك ؟",
            "أصعب انتظار ؟",
            "أجمل بيت شعر سمعته ...",
            "مودك الحين ؟",
            "عندك صديق يحمل نفس اسمك ؟",
            "محادثة ولا مكالمة ؟",
            "كم مره يتقلب مزاجك باليوم ؟",
            "اكثر شخص يسوي فيك مقالب ؟",
            "مكان تبي تكون فيه الحين ؟.",
            "كم من عشرة تحب مهنة التدريس ؟",
            "شنو تتوقع بتصير بعد 10 سنين ؟ ",
            "متى تحب الطلعة ؟",
            "أغرب شي اشتهيت تأكله فجأة ؟",
            "اخر مره بكيت متى ؟",
            "اكثر شخص يقفل بوجهك اذا كلمك ؟",
            "كثر شخص يكرفك ؟",
            "تدخل بنقاش بموضوع ماتفهم فيه شيء ولا تسكت وتسمع بس ؟",
            "عمرك طحت بمكان عام ؟",
            "شخص يعرف عنك كل شي تقريباً ؟",
            "اكثر واحد يرسلك بالديسكورد ؟",
            "إيش اللي قدامك الحين ؟",
            "من النوع اللي تعتمد على غيرك ولا كل شي تسويه بنفسك ؟",
            "تقدر تعيش يوم كامل بدون نت ؟",
            "مع او ضد : الاعتراف بـ شيء في قلبك دام طويلاً ؟",
            "أبوك إيش يقرب لأمك ؟",
            "اكثر مدة جلستها بدون نت ؟",
            "لو رجعناك خمس سنين هل كنت تتوقع ان حياتك بتكون نفس وضعك الحين ؟",
            "تتقبل النصيحة من أي أحد ؟",
            "متى لازم تقول لا ؟",
            "أكثر ماده تحبها دراسياً والسبب؟.",
            "إيش نوع قهوتك المفضلة ؟",
            "شخص تشوفه بشكل يومي غير اهلك ؟",
            "شخص تحب ابتسامتة ؟",
            "من الاشياء اللي تجيب لك الصداع ؟",
            "وش تحب تسوي وقت فضاوتك ؟.",
            "كم تعطي نفسك من عشرة بالجدية بحياتك ",
            "أكثر شي يعتمدون عليك فيه ؟",
            "اكثر صفة عندك ؟",
            "كيف تعبر عن عصبيتك ؟",
            "كم داخل سيرفر فالديسكورد ؟",
            "حصلت الشخص اللي يفهمك ولا باقي ؟",
            "تفضل .. العيون الناعسة ... العيون الواسعة ؟",
            "اشياء تغيرت تظرتك لها",
            "الرقم السري حق جوالك ...",
            "لو قررت تقفل جوالك يوم كامل مين تتوقع أنه يفتقدك ؟",
            "اخر هوشه جلدت ولا انجلدت ؟",
            "نصيحه صغيرة من واقع تجربتّك؟.",
            "شخص يكلمك بشكل يومي ؟",
            "أسم وانطباعك عنه ؟",
            "العصر إيش كنت تسوي ؟",
            "كم من عشرة تعطي اهتمامك بدراستك أو عملك ؟",
            "كيف تفرغ غضبك بالعادة ؟",
            "أطول مدة قضيتها بعيد عن أهلك ؟",
            "شخص مستحيل تمسك ضحكتك معاه؟",
            "حاجة دايم تضيع منك ؟",
            "تجامل احد على حساب مصلحتك ؟",
            "كم لك فـ الديسكورد ؟",
            "اخر شخص تهاوشت معه مين ؟",
            "اكثر شيء تكره تنتظره ؟",
            "اخر مطعم اكلت منه ؟",
            "اكثر شيء تحبه بـ شكلك ؟",
            "تنام بـ اي مكان ، ولا بس غرفتك ؟",
            "اكتب اول كلمة جات في بالك الحين ؟",
            "تهمك التفاصيل ولا الزبدة من الموضوع ؟",
            "شيء واحد .. م عاد يهمك كثر اول ؟",
            "كم تقييمك لـ طبخك من 10 ، ولا م تطبخ ؟",
            "اتفه شيء ارسلوك عشانه ؟",
            "فن تحبه كثير ؟",
            "اكثر سوالفك عن ...؟",
            "صفة موجودة في جميع افراد عائلتك ؟",
            "شخص م تقدر تكذب عليه ؟",
            "كم من 10 تحس بـ الطفش ؟",
            "من النوع الي تجيك الردود القوية بعد الهوشة ولا فـ وقتها ؟",
            "تحب تجرب الاشياء الجديدة ، ولا تنتظر الناس يجربونها اول ؟",
            "وش اغبى شيء سويته ؟",
            "اكثر كلمة الناس تقولها عن شخصيتك ؟",
            "مراقبة شخص تركته .. فضول ولا بقايا مشاعر ؟",
            "برنامج كرهته الفترة هاذي",
            "مشهور ، او مشهورة .. يشبهونك فيه",
            "بالغالب وش تسوي فـ الويكند ؟",
            "وش اسم الحي الي ساكن فيه ؟",
            "اكثر شيء تخاف منه ؟",
            "عاده لاتستطيع تركها ؟ ",
            "كم من الوقت تحتاج عشان تصحصح من بعد م صحيت من النوم ؟",
            "اذا حسيت بـ غيرة تتكلم ولا تسكت ؟",
            "مع او ضد ... اقاربك يعرفون عن حساباتك في برامج التواصل ؟",
            "اخر مره سافرت بالطائرة والى وين؟",
            "وش اليوم الي تكرف فيه كثير ؟",
            "تفضل .. الاعمال الحرة ولا الوظيفة ؟",
            "حاجة تشوف نفسك مبدع فيها ؟",
            "ماركتك المفضلة ؟",
            "منشن ... اكثر شخص تثق فيه ؟",
            "اذا انسجنت وش تتوقع بتكون التهمة الي عليك ؟",
            "تعطي الناس فرصة تتقرب منك ؟",
            "منشن .. الشخص الي يستحق تدخل الديسكورد عشانه ..",
            "متى اخر مره نمت اكثر من 12 ساعة ؟",
            "رائحة عطر مدمن عليها ..",
            "وش تحس انك تحتاج الفترة هاذي ؟",
            "كم من 10 البرود فيك ؟",
            "وش اكثر فاكهة تحبها ؟",
            "اصعب وظيفة في نظرك ؟",
            "شيء بسيط قادر على حل كل مشاكلك ..",
            "اذا جلست عند ناس م تعرفهم .. تكتفي بالسكوت ، ولا تتكلم معهم ؟",
            "تتحمل المزح الثقيل ؟",
            "من النوع الي تنام فـ طريق السفر ؟",
            "لو شلنا من طولك 100 كم يبقى من طولك ؟",
            "موقفك من شخص أخفى عنك حقيقة ما، تخوفًا من خسارتك؟ ",
            "اكثر شخص ينرفزك الي ؟",
            "تعرف تتصرف في المواقف العصبة ؟",
            "متى حسيت انك مختلف عن الي غيرك ؟",
            "اصعب مرحلة دراسية مرت عليك ؟",
            "سويت شيء بالحياة وانت مو مقتنع فيه ؟",
            "اخر مره ضربوك فيها ... ووش كان السبب ؟",
            "من الاشياء الي تجيب لك الصداع ؟",
            "مين اول شخص تكلمه اذا طحت بـ مصيبة ؟",
            "مع او ضد : النوم افضل حل لـ مشاكل الحياة ...",
            "تجامل ولا صريح ؟",
            "تفضل المواد الي تعتمد على الحفظ ولا الفهم ؟",
            "صفة تخليك تكره الشخص مهما كان قربه منك ؟",
            "جربت احد يعطيك بلوك وانت تكتب له ؟",
            "تهتم بـ معرفة تاريخ ميلاد الي تحبهم ؟",
            "فيه شيء م تحب تطلبه حتى لو كنت محتاجة ؟",
            "دائما قوة الصداقة بـ ... ؟",
            "اخر شخص قالك كلمة حلوة ..",
            "كم من 10 الي تتوقعه يصير ؟",
            "اذا كنت بنقاش مع شخص وطلع الحق معه تعترف له ولا تصر على كلامك ؟",
            "فيه شخص تكرهه بشكل كبير ؟ ولك جرأة تمنشن اسمه ؟",
            "كيف الجو عندكم اليوم ؟",
            "ترتيبك بالعائلة ؟",
            "تسمع شيلات ؟",
            "تفضل السفر فـ الشتاء ولا الصيف ؟",
            "مع او ضد : الهدية بـ معناها وليس بـ قيمتها",
            "عندك صحبة من اشخاص خارج دولتك",
            "عندك صحبة من اشخاص خارج دولتك ؟",
            "تحب اصوات النساء فـ الاغاني ولا الرجال",
            "وش اول جوال شريته ؟",
            "وش النوع الي تحبه ف الافلام ؟",
            "اكثر مكان تحب تجلس فيه فالبيت ؟",
            "صفة قليل تحصلها فـ الناس حالياً ؟",
            "من النوع الي تعترف ولا تجحد ؟",
            "اول شخص تكلمه اذا صحيت من النوم ؟",
            "وش اجمل لهجة عرببية بالنسبة لك ؟",
            "اخر اتصال من مين كان ؟",
            "اجمل مدينة بدولتك ؟",
            "شاعرك المفضل ؟",
            "كم مره تشحن جوالك باليوم",
            "لو كنت مؤلف كتاب .. وش راح يكون اسمه ؟",
            "اطول مدة قضيتها بدون اكل ..",
            "كم من 10 نسبة الكسل فيك هالايام ؟",
            "نومك خفيف ولا ثقيل ؟",
            "كم من عشرة تشوف صوتك حلو ؟",
            "تجيك الضحكة بوقت غلط ؟",
            "تفضل التسوق من الانترنت ، ولا الواقع ؟",
            "اغرب اسم مر عليك ؟",
            "وش رقمك المفضل ؟",
            "شيء تبيه يصير الحين ...",
            "شاي ولا قهوة ؟",
            "صفة يشوفونها الناس سيئة ، وانت تشوفها كويسه",
            "لون تكرهه ...",
            "وظيفة تحسها لايقة عليك ...",
            "كم من 10 كتابتك بالقلم حلوة ؟",
            "اكلة ادمنتها الفترة ذي ...",
            "اجمل مرحلة دراسية مرت عليك ..",
            "اكثر شيء تكرهه فالديسكورد ..",
            "شيء مستحيل انك تاكله ...",
            "وش رايك بالي يقرأ ولا يرد ؟",
            "اسمك بدون اول حرفين ..",
            "متى تكره الطلعة ؟",
            "شخص من عائلتك يشبهونك فيه ...",
            "اكثر وقت تحب تنام فيه ...",
            "تنتظر احد يجيك ؟",
            "اسمك غريب ولا موجود منه كثير ؟",
            "وش الشيء الي يكرهه اقرب صاحب لك ؟",
            "كم من 10 حبك للكتب ؟",
            "جربت الشهرة او تتمناها ؟",
            "مين اقرب شخص لك بالعائلة ؟",
            "شيء جميل صار لك اليوم ؟",
            "كلمتك اذا احد حشرك بالنقاش ...",
            "اعمال يدوية نفسك تتقنها . ",
            "وش الي يغلب عليك دائما .. قلبك ولا عقلك ؟",
            "صفة تحمد الله انها مو موجودة في اصحابك ...",
            "كم وجبة تاكل فاليوم الفترة هاذي ؟",
            "جربت دموع الفرح ؟ وش كان السبب ؟",
            "لو فقط مسموح شخص واحد تتابعه فالسناب مين بيكون ؟",
            "‏لو حطوك بمستشفى المجانين كيف تقنعهم إنك مو مجنون ؟.",
            "اكثر شيء تحبه فالشتاء ...",
            "شيء ودك تتركه ...",
            "كم تعطي نفسك من 10 فاللغة الانجليزية ؟",
            "شخص فرحتك مرتبطة فيه ...",
            "اكتب اسم .. واكتب كيف تحس بيكون شكله ...",
            "متى اخر مره قلت ليتني سكت ؟",
            "ممكن تكره احد بدون سبب ؟",
            "اكثر وقت باليوم تحبه ...",
            "اكثر شيء حظك سيء فيه ...",
            "متى صحيت ؟",
            "كلمة صعب تقولها وثقيلة عليك ...",
            "ردك الدائم على الكلام الحلو ...",
            "سؤال دايم تتهرب من الاجابة عليه ...",
            "مين الشخص اللي مستعد تأخذ حزنه بس م تشوفه حزين ؟.",
            "جربت تروح اختبار بدون م تذاكر ؟",
            "كم مرة غشيت ف الاختبارات ؟",
            "وش اسم اول شخص تعرفت عليه فالديسكورد ؟",
            "تعطي فرصة ثانية للشخص الي كسرك ؟",
            "لو احتاج الشخص الي كسرك مساعدة بتوقف معه ؟",
            "@منشن... شخص ودك تطرده من السيرفر ...",
            "دعاء له اثر إبجابي في حياتك ...",
            "قل حقيقه عنك ؟",
            "انسان م تحب تتعامل معه ابد",
            "اشياء اذا سويتها لشخص تدل على انك تحبه كثير ؟",
            "الانتقاد الكثير يغيرك للافضل ولا يحطمك ويخليك للأسوأ ؟",
            "كيف تعرف اذا هذا الشخص يكذب ولا لا ؟",
            "مع او ضد : العتاب على قدر المحبة ...",
            "شيء عندك اهم من الناس",
            "تتفاعل مع الاشياء اللي تصير بالمجتمع ولا ماتهتم ؟.",
            "وش الشيء الحلو الي يميزك عن غيرك ؟",
            "كذبة كنت تصدقها وانت صغير ..",
            "@منشن .. شخص تخاف منه اذا عصب ...",
            "كلمة بـ لهجتك تحس م احد بيعرفها ...",
            "كمل ... انا من الاشخاص الي ...",
            "تراقب احد بالديسكورد ؟",
            "كيف تعرف ان هالشخص يحبك ؟",
            "هواية او تجربة كان ودك تستمر و تركتها ؟",
            "الديسكورد اشغلك عن حياتك الواقعية ؟",
            "اكمل ... تستمر علاقتك بالشخص اذا كان ...",
            "لو احد قالك اكرهك وش بتقول له ؟",
            "مع او ضد : عامل الناس كما يعاملوك ؟",
            "ارسل اخر صورة فـ الالبوم ...",
            "الصق وارسل اخر شيء نسخته ...",
            "ماهي اخر وجبة اكلتها ",
            "اكثر شيء تحس انه مات ف مجتمعنا",
            "برأيك ماهو افضل انتقام ...",
            "اكثر ريحة تجيب راسك ...",
            "شعور ودك يموت ...",
            "عمرك فضفضت لـ شخص وندمت ؟",
            "تقدر تتحمل عيوب شخص تحبه ؟",
            "يكبر الشخص ف عيونك لما ...",
            "وش تقول للشخص الي معك دائماً ف وقت ضيقتك ؟",
            "مقولة او حكمة تمشي عليها ...",
            "منشن ... شخص اذا وضعه على الجرح يلتهب زيادة",
            "منشن ... شخص يعجبك كلامه و اسلوبه ...",
            "لو السرقة حلال ... وش اول شيء بتسرقه ؟",
            "مع او ضد : المرأة تحتاج لرجل يقودها ويرشدها ...",
            "مع او ضد : لو دخل الشك ف اي علاقة ستنتهي ...",
            "منشن... اي شخص واوصفه بـ كلام بسيط ...",
            "مع او ضد : قلة العلاقات راحة ...",
            "لو خيروك : تعض لسانك بالغلط ، ولا يسكر على صبعك الباب؟",
            "كلمة غريبه و معناها ...",
            "نصيحة تقدمها للشخص الثرثار ...",
            "مع او ضد :  مساعدة الزوجة في اعمال المنزل مهما كانت ...",
            "منشن... شخص يجيك فضول تشوف وجهه ...",
            "كلمة لـ شخص عزيز عليك ...",
            "اكثر كذبة تقولها ...",
            "معروف عند اهلك انك ...",
            "وش اول طريقة تتبعها اذا جيت تراضي شخص",
            "ع او ضد : ما تعرف قيمة الشخص اذا فقدته ...",
            "تحب تختار ملابسك بنفسك ولا تحب احد يختار معك ...",
            "وش اكثر شيء انجلدت بسببه وانت صغير ؟",
            "فـ اي برنامج كنت قبل تجي الديسكورد ؟",
            "تنسد نفسك عن الاكل لو زعلت ؟",
            "وش الشيء الي تطلع حرتك فيه و زعلت ؟",
            "مع او ضد : الصحبة تغني عن الحب ... ",
            "منشن... اخر شخص خلاك تبتسم",
            "لو نطق قلبك ماذا سيقول ...",
            "ماذا يوجد على يسارك حالياً ؟",
            "مع او ضد : الشخص الي يثق بسرعة غبي ...",
            "شخصية كرتونية تأثرت فيها وانت صغير ...",
            "مع او ضد : الاهتمام الزائد يضايق",
            "لو خيروك : تتزوج ولا تكمل دراستك ...",
            "منشن... لو بتختار شخص تفضفض له مين بيكون ؟",
            "كمل : مهما كبرت بخاف من ....",
            "اخر عيدية جاتك وش كانت ...",
            "وش حذفت من قاموس حياتك ...",
            "شيء تتمنى م ينتهي ...",
            "اكره شعور ممكن يحس فيه الانسان هو ...",
            "مع او ضد : يسقط جمال المراة بسبب قبح لسانها ...",
            "ماهي الخسارة في نظرك ...",
            "لو المطعم يقدم الوجبه على حسب شكلك وش راح تكون وجبتك ؟",
            "مع او ضد : يموت الحب لو طال الغياب",
            "وش الشيء الي يحبه اغلب الناس وانت م تحبه ..",
            "تحدث عن نفسك ؟",
            "اقوى جملة عتاب وصلتك",
            "على ماذا ندمت ؟",
            "اخر مرة انضربت فيها من احد اهلك ، ولماذا ؟",
            "افضل طريقة تراضي فيها شخص قريب منك",
            "لو بإمكانك تقابل شخص من الديسكورد مين بيكون ؟",
            "كمل : كذاب من يقول ان ...",
            "طبعك صريح ولا تجامل ؟",
            "مين اقرب لك ؟ اهل امك ، اهل ابوك  ...",
            "وش لون عيونك ؟",
            "مع او ضد : الرجال اكثر حقداً من النساء",
            "مع او ضد : ينحب الشخص من اهتمامه",
            "@منشن: شخص تقوله اشتقت لك",
            "بصراحة : تحب تفضفض وقت زعلك ، ولا تنعزل ؟",
            "مع او ضد : حبيبك يطلب منك حذف اصحابك بحكم الغيرة",
            "متى تحس بـ شعور حلو ؟",
            "لو حياتك عبارة عن كتاب .. وش بيكون اسمه ؟",
            "@منشن: شخص واسأله سؤال ...",
            "كم مره سويت نفسك غبي وانت فاهم ،  ومع مين ؟",
            "اكتب شطر من اغنية او قصيدة جا فـ بالك",
            "كم عدد الاطفال عندكم فالبيت ؟",
            "@منشن : شخص وعطه وظيفة تحس تناسبه",
            "اخر مكالمة فـ الخاص كانت مع مين ؟",
            "عمرك ضحيت باشياء لاجل شخص م يسوى ؟",
            "كمل : حلو يومك بـ وجود ...",
            "مع او ضد : المرأة القوية هي اكثر انسانه انكسرت",
            "نصيحة تقدمها للغارقين فالحب ...",
            "مبدأ تعتمد عليه فـ حياتك",
            "ترد بالمثل على الشخص لو قذفك ؟",
            "شيء مهما حطيت فيه فلوس بتكون مبسوط",
            "@منشن: اكثر شخص يفهمك",
            "تاريخ ميلادك + هدية بخاطرك تجيك",
            "كم كان عمرك لما اخذت اول جوال ؟",
            "عمرك كتبت كلام كثير بعدين مسحته ، مع مين كان؟",
            "برأيك : وش اكثر شيء يرضي البنت الزعلانه ؟",
            "مساحة فارغة (..............) اكتب اي شيء تبين",
            "تترك احد عشان ماضيه سيء ؟",
            "تهتم بالابراج ، واذا تهتم وش برجك ؟",
            "لو ستبدأ حياتك من جديد ، وش راح تغير بـ نفسك ؟",
            "تتوقع فيه احد حاقد عليك ويكرهك ؟",
            "وش يقولون لك لما تغني ؟",
            "مين المغني المفضل عندك ؟",
            "ميزة ودك يضيفها البرنامج",
            "وش الي مستحيل يكون لك اهتمام فيه ؟",
            "البنت : تتزوجين احد اصغر منك ",
            "الرجل : تتزوج وحده اكبر منك",
            "احقر الناس هو من ...",
            "البنت : وش تتمنين تكون وظيفة زوجك ",
            "الرجل : وش تتمنى وظيفة زوجتك",
            "برأيك : هل الانتقام من الشخص الذي اخطأ بحقك راحة ؟",
            "اهم شيء يكون معك فـ كل طلعاتك ؟",
            "وش الخدمة الالكترونية الي تتمنى تصير ؟",
            "كلمة تخليك تلبي الطلب حق الشخص بدون تفكير",
            "وش الفايدة الي اخذتها من الديسكورد ؟",
            "مع ام ضد : غيرة البنات حب تملك وانانية",
            "هل سبق ان ندمت انك رفضت شيء ، وش كان ؟",
            "تشوف انك قادر على تحمل المسؤولية ؟",
            "مع او ضد : الناس يفضلون الصداقة وعندما يأتي الحب يتركون الصداقة",
            "اعلى نسبة جبتها ف حياتك الدراسية",
            "تحب احد يتدخل ف امورك الشخصية  ؟",
            "لو واحد يتدخل ف امورك وانت م طلبت منه وش بتقوله ؟",
            "تاخذ بنصيحة  الاهل ام من الاصحاب ؟",
            "فيه شيء م تقدر تسيطر عليه ؟",
            "@منشن : شخص تحب سوالفه",
            "وش الكذبة المعتادة الي تسويها لو بتقفل من احد ؟",
            "@منشن: الشخص الي عادي تقوله اسرارك",
            "لو زعلت بقوة وش بيرضيك ؟",
            "كلمة تقولها لـ بعض الاشخاص في حياتك",
            "ندمت انك اعترف بمشاعرك لـ شخص",
            "وش الاكلة المفضلة عندك ؟",
            "وش تتخيل يصير معك فـ المستقبل ؟",
            "اسم الطف شخص مر عليك الكترونياً",
            "مع او ضد : الاستقرار النفسي اهم استقرار",
            "مع او ضد : كل شيء راح يتعوض",
            "برأيك : وش الشيء الي مستحيل يتعوض ؟",
            "تفضل : الدجاج ، اللحم ، السمك",
            "تفضل : الصباح ، الليل",
            "كمل : النفس تميل لـ ...",
            "عندك القوة انك تبين اعجابك لـ شخص ؟",
            "مع او ضد : الرد المتأخر يهدم العلاقات",
            "مشروبك المفضل ...",
            "اقوى كذبة كذبتها على اهلك",
            "@منشن : شخص واكتب شعور نفسك يجربه",
            "وش ردة فعلك من الشخص الي يرد عليك بعد ايام او ساعات ...",
            "كيف تعبر عن عصبيتك ؟",
            "عمرك بكيت على شخص مات في مسلسل ؟",
            "تتأثر بالمسلسلات او الافلام وتتضايق معهم ؟",
            "لو خيروك : بين شخص تحبه وشخص يحبك",
            "اقسى نهاية عندك ...",
            "مع او ضد : كل م زاد المال في الزواج زادت السعادة",
            "لو سمح لك بسرقة شيء ويكون ملك لك .. ماذا ستسرق ؟",
            "تقدر تنام وخاطرك مكسور ؟",
            "برأيك : اقرب لهجة عربية قريبة للفصحى ؟",
            "مر عليك شخص ف حياتك مستحيل انك تسامحه ",
            "عندك صاحب له معك اكثر من 5 سنين ؟",
            "وش معنى اسمك ؟",
            "عندك الصاحب الي تقول للناس اتحداكم تفرقونا ؟",
            "تقييمك لـ صوتك ف الغناء من 10",
            "كم طولك ؟",
            "كم وزنك ؟",
            "وش طموحك بالحياة ؟",
            "لو بيدك توقف شيء يصير ، وش راح توقف ؟",
            "وش اسم قبيلتك ؟",
            "اقرب فعل لقلبك ؟",
            "وش نوع جوالك ؟",
            "وش المطعم المفضل عندك ؟",
            "مين الشخص الي محلي حياتك ؟",
            "انا مدمن على ...",
            "مع او ضد : الصدق هو سر استمرار العلاقات فترة طويلة",
            "تكون اجمل شخص اذا ...",
            "شكلك يعطي لأي جنسية ؟",
            "وش اكثر دولة تحب الشعب حقها ؟",
            "اول بيت تزوره فالعيد ..",
            "جمال المراة يكمن في ...",
            "مشهور تعجبك سناباته ..",
            "مشهور تكرهه",
            "يكفيك عطر واحد ولا تحب تحط اكثر من عطر ؟",
            "مرة جاك احد بيذكرك فيه وانت ناسي ؟",
            "لو احد بيذكرك فيه وانت ناسي بتسلك له ؟",
            "اغنيتك المفضلة ...",
            "مع او ضد : لو م اخذت شيء معك وقت زيارة احد انت مقصر",
            "يهمك ملابسك تكون ماركة ؟",
            "مع او ضد : او اهتزت مكانة الشخص مستيحل ترجع",
            "لو رجع لك شخص تعرفه بعد علاقته بالخيانة ، راح ترجع نفس اول ؟",
            "صفة لا تتمنى ان تكون فـ عيالك",
            "وش اسم قروبك انت واصحابك المقربين ؟",
            "وش اسم قروب عائلتك فالواتس اب ؟",
            "مع او ضد : تكون الزوجة عندما تشترط خادمة في العقد سيئة",
            "لعبة ندمت انك لعبتها ...",
            "مع او ضد : يمكن للبنت تغيير رأي الرجل بسهولة",
            "كلمة او عبارة مستحيل تنساها",
            "ارسل اكثر ايموجي تحبه",
            "شيء تتمنى يتحقق",
            "مع او ضد : الدنيا لم تتغير ، بل النفوس التي تغيرت",
            "وش جمع اسمك ؟",
            "كلمة لـ شخص زعلان منك ...",
            "عادة غريبة تسويها ..",
            "تحب ريحة الحناء ؟",
            "نومك : ثقيل ولا خفيف",
            "اكثر شيء يرفع ضغطك",
            "اكتب تاريخ مستحيل تنساه",
            "لو حظك يباع ، بكم بيكون ؟",
            "@منشن : شخص تشوف انه يجذبك",
            "البنت : عادي تحضنين اخوك ؟",
            "الولد : عادي تحضن ابوك ؟",
            "كلمة تحب تسمعها حتى لو كنت زعلان",
            "قوة الاستيعاب عندك من 10",
            "افضل نوع عطر استخدمته",
            "وش بتختار اسم لأول مولود لك ؟",
            "متى تصير نفسية ؟",
            "كيف ينطق الطفل اسمك ؟",
            "تشوف نفسك شخص عاطفي ولا علاقني ؟",
            "متى لازم تقول لا ؟",
            "تحب توجه الكلام عن طريق ( الكتابة ، الصوت )",
            "مين اقرب لك : (خوالك ، عمامك )",
            "تحب تتعرف على ناس جديدة ولا اكتفيت بالي عندك ؟",
            "شيء كل م تذكرته تبتسم ...",
            "كم قروب واتس داخل ؟",
            "كم سيرفر داخل فالديسكورد ؟",
            "مع او ضد : المسامحة بعد الخيانة ...",
            "وش الامنية الي ودك تتحقق ؟",
            "كيف تتصرف مع الشخص الفضولي ؟",
            "الرجل : متى تفقد البنت انوثتها",
            "ماهي اسباب نهاية العلاقات ؟",
            "@منشن : شخص ودك تعطيه كتم ",
            "مين الي تحب يكون مبتسم دائما",
            "حصلت الشخص الي يفهمك ولا باقي ؟",
            "كم تحتاج وقت عشان تصحصح من نومك ؟",
            "كيف تعالج الغيرة الزائدة ؟",
            "مع او ضد : كل شيء حلو يكون فالبداية فقط",
            "اطول مدة قضيتها بعيد عن اهلك",
            "شيء دايم يضيع منك",
            "اغنية ناشبه ف مخك",
            "رسالة للناس الي بيدخلون حياتك",
            "جملة او كلمة تكررها",
            "اكثر اغنية تكرهها ؟",
            "صوت مغني م تحبه",
            "مع او ضد : الغيرة بين الاصدقاء",
            "اكثر وقت تحب تنام فيه",
            "وش اثقل مشوار ممكن تسويه ؟",
            "اقرب شخص لك بالعائلة",
            "اخر مكان سافرت له",
            "مع او ضد : حنا اكثر الناس عندنا حكم لكن م نطبقها",
            "مع و ضد : العتاب اكثر من مره دليل على ان الشخص م يقدرك",
            "كم مشاهداتك باسناب؟ ",
            "مع او ضد : اكثر من في الديسكورد أُناس يتصنعون",
            "شيء نفسك تعيشه من جديد",
            "كلمة تحسسك بالامان",
            "كم تعطي نفسك من 10 فـ تعاملك مع مشاكلك",
            "مع او ضد : اكثر من يحلون مشاكل الناس ، هم اكثر الناس لديهم مشاكل", ]


@sbb_b.on(admin_cmd(pattern="اعتراف$"))
async def ithker(knopis):
    await knopis.edit(choice(samir4))
