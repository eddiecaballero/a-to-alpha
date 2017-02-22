#coding: utf8

from PIL import Image
import tesserocr
from tesserocr import PyTessBaseAPI
from yandex_translate import YandexTranslate

#Settings
translate = YandexTranslate('Add your API Key here')
sourceLanguage = "el" #Unfortunately Yandex language detection is unrealiable so best to be explicit.
targetLanguage = "en"
imageToRecognize = "greek.png"

#https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#languages
#https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#languages
yandexToTesseractLanguages = {
	"az":"aze", #Azerbaijan - Latin(aze), Cyrilic(aze_cyrl)
	"am":"amh", #Amharic
	"en":"eng", #English - Modern(eng), English Middle 1100-1500(enm)
	"ar":"ara", #Arabic
	"af":"afr", #Afrikaans
	"eu":"eus", #Basque
	"be":"bel", #Belarusian
	"bn":"ben", #Bengali
	"bg":"bul", #Bulgarian
	"bs":"bos", #Bosnian
	"cy":"cym", #Welsh
	"hu":"hun", #Hungarian
	"vi":"vie", #Vietnamese
	"ht":"hat", #Haitian - Haitain(hat), Haitain Creole(hat)
	"gl":"glg", #Galician
	"nl":"nld", #Dutch - Dutch(nld), Flemish(nld)
	"el":"ell", #Greek - Modern(ell), Greek Ancient to 1453(grc)
	"ka":"kat", #Georgian - Modern(kat), Georgian Old(kat_old)
	"gu":"guj", #Gujarati
	"da":"dan", #Danish - Modern(dan), Danish Fraktur(dan_frak)
	"he":"heb", #Hebrew
	"yi":"yid", #Yiddish
	"id":"ind", #Indonesian
	"ga":"gle", #Irish
	"it":"ita", #Italian - Modern(ita), Italian Old(ita_old)
	"is":"isl", #Icelandic
	"es":"spa", #Spanish - Modern(spa), Spanish Castilian Old(spa_old)
	"kk":"kaz", #Kazakh
	"kn":"kan", #Kannada
	"ca":"cat", #Catalan - Catalan(cat), Valencian(cat)
	"ky":"kir", #Kyrgyz - Kyrgyz(kir), Kirghiz(kir)
	"zh":"chi_sim", #Chinese - Chinese Simplified(chi_sim), Chinese Traditional(chi_tra)
	"ko":"kor", #Korean
	"la":"lat", #Latin
	"lv":"lav", #Latvian
	"lt":"lit", #Lithuanian
	"ml":"mal", #Malayalam
	"mt":"mlt", #Maltese
	"mk":"mkd", #Macedonian
	"mr":"mar", #Marathi
	"de":"deu", #German - Modern(deu), German Fraktur(deu_frak)
	"ne":"nep", #Nepali
	"no":"nor", #Norwegian
	"pa":"pan", #Punjabi
	"fa":"fas", #Persian
	"pl":"pol", #Polish
	"pt":"por", #Portuguese
	"ro":"ron", #Romanian
	"ru":"rus", #Russian
	"ceb":"ceb", #Cebuano
	"sr":"srp", #Serbian - Cyrilic(srp), Serbian Latin(srp_latn)
	"si":"sin", #Sinhala
	"sk":"slk", #Slovakian - Modern(slk), Slovak Fraktur(slk_frak)
	"sl":"slv", #Slovenian
	"sw":"swa", #Swahili
	"tg":"tgk", #Tajik
	"th":"tha", #Thai
	"tl":"tgl", #Tagalog
	"ta":"tam", #Tamil
	"te":"tel", #Telugu
	"tr":"tur", #Turkish
	"uz":"uzb", #Uzbek - Latin(uzb), Uzbek Cyrilic(uzb_cyrl)
	"uk":"urk", #Ukrainian
	"ur":"urd", #Urdu
	"fi":"fin", #Finnish
	"fr":"fra", #French - Modern(fra), Frankish(frk), French Middle ca.1400-1600(frm)
	"hi":"hin", #Hindi
	"hr":"hrv", #Croatian
	"cs":"ces", #Czech
	"sv":"swe", #Swedish
	"et":"est", #Estonian
	"eo":"epo", #Esperanto
	"jv":"jav", #Javanese
	"ja":"jpn" #Japanese
}

with tesserocr.PyTessBaseAPI(lang=yandexToTesseractLanguages[sourceLanguage]) as api:
	api.SetImageFile(imageToRecognize)
	textRecognized = api.GetUTF8Text().strip()
print textRecognized

translateDirection = sourceLanguage + "-" + targetLanguage
print (translate.translate(textRecognized, translateDirection)['text'][0]).encode('UTF-8')