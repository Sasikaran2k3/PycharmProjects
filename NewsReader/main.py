import time
import pyttsx3
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = Options()
#options.add_experimental_option("debuggerAddress","localhost:1234")
options.add_argument(r'--user-data-dir=E:\Chatterbot\Selenium Browser')
services = Service(r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=options)
browser.maximize_window()
browser.implicitly_wait(20)

#def getNews(Url="https://gadgets360.com/trends#pfrom=desktop-lhs-trending"):
"""
    browser.get(Url)
    cat= Select(browser.find_element(By.CSS_SELECTOR,'select[class="form-control ng-untouched ng-pristine ng-valid"]'))
    cat.select_by_value("1")
    StAtr = ['AN', 'AP', 'AR', 'AS', 'BI', 'CH', 'CG', 'DN', 'DD', 'DL', 'GO', 'GJ', 'HA', 'HI', 'JK', 'JH', 'KA', 'KE',
             'LD', 'LK', 'MP', 'MH', 'MA', 'ME', 'MI', 'NG', 'OR', 'PY', 'PJ', 'RJ', 'SI', 'TN', 'TE', 'TR', 'UT', 'UP',
             'WB']
    Dummy = ['AN','DD']
    Dist = [['Andamans,Nicobars'], ['Anantapur,Chittoor,Cuddapah,East Godavari,Guntur,Kadapa Municipal Corporation,Kakinada Mpl.Corp.,Krishna,Kurnool,Nellore,Prakasam,Srikakulam,Visakhapatnam,Vizianagaram,West Godavari'], ['Anjaw,Changlang,Dibang Valley,East Kameng,East Siang,Kamle,Kra Dadi,Kurung Kumey,Leparada,Lohit,Longding,Lower Dibang Valley,Lower Subansiri,Lower Subansiri,Namsai,Pakke Kessang,Papum Pare,Shi Yomi,Siang,Tawang,Tirap,Upper Siang,Upper Subansiri,West Kameng,West Siang'], ['Baksa,Barpeta,Biswanath,Bongaigaon,Cachar,Charaideo,Chirang,Darrang,Dhemaji,Dhubri,Dibrugarh,Dima Hasao,Goalpara,Golaghat,Hailakandi,Hojai,Jorhat,Kamrup Dist.,Kamrup Metropolitan Dist.,Karbi Anglong,Karimganj,Kokrajhar,Lakhimpur,Majuli,Marigaon,Nagaon,Nalbari,Sivasagar,Sonitpur,South Salmara Mancachar,Tinsukia,Udalguri,West Karbi Anglong'], ['Araria,Arwal,Aurangabad,Banka,Begusarai,Bhagalpur,Bhojpur,Buxar,Darbhanga,Gaya,Gopalganj,Jamui,Jehanabad,Kaimur (Bhabua),Katihar,Khagaria,Kishanganj,Lakhisarai,Madhepura,Madhubani,Munger,Muzaffarpur,Nalanda,Nawada,Pashchim Champaran,Patna,Purba Champaran,Purnia,Rohtas,Saharsa,Samastipur,Saran,Sheikhpura,Sheohar,Sitamarhi,Siwan,Supaul,Vaishali'], ['Chandigarh'], ['Balod,Balodabazar,Balrampur,Bastar,Bemetara,Bijapur,Bilaspur,Dantewada,Dhamtari,Durg,Gariyaband,Gurela-Pendra-Marwahi,Janjgir - Champa,Jashpur,Kabirdham,Kanker,Kawardha,Kondagaon,Korba,KOREA,Mahasamund,Mungeli,Narayanpur,Raigarh,Raipur,Rajnandgaon,Sukma,Surajpur,Surguja'], ['Dadra & Nagar Haveli'], ['Daman,Diu'], ['Central,East,New Delhi,North,North East,North West,Shahdara,South,South East,South West,West'], ['North Goa,South Goa'], ['Ahmedabad,Amreli,Amreli Municipality,Anand,Arvalli,BANASKANTHA,Bharuch,Bhavnagar,BHUJ(KUTCHH),Botad Rural,Chhota Udaipur,Dahod Municipality,Dang,Devbhumi Dwarka,Dohad,Gandhidham Municipality,Gandhinagar,Gir Somnath,Godhra Municipality,GODHRA(PANCHMAHAL),HIMMATNAGAR(SABARKANTHA),Jamnagar,Junagadh,Kalol Municipality,Mahesana,MAHISAGAR,MORBI,NADIAD(KHEDA),Narmada,Navsari,Patan,Porbandar,Rajkot,Rajkot Municipal Corporation,Surat,Surat Municipal Corporation,Surendranagar,Tapi,Vadodara,Vadodara Municipal Corporation,Valsad,VYARA(TAPI)'], ['Ambala,Bhiwani,Charkhi Dadri,Faridabad,Fatehabad,Gurugram,Hisar,Jhajjar,Jind,Kaithal,Karnal,Kurukshetra,Mahendragarh,Mewat,Palwal,Panchkula,Panipat,Rewari,Rohtak,Sirsa,Sonipat,Yamunanagar'], ['Bilaspur,Chamba,Hamirpur,Kangra,Kinnaur,Kullu,Lahul & Spiti,Mandi,Shimla,Shimla Muncipal Corporation,Sirmaur,Solan,Una'], ['Anantnag,Badgam,Bandipore,Baramula,Doda,Ganderbal,Jammu,Kathua,kishtwar,Kulgam,Kupwara,Poonch,Pulwama,Punch,Rajauri,Ramban,Reasi,Samba,Shopian,Srinagar,Udhampur'], ['Bokaro,Chatra,Deoghar,Dhanbad,Dumka,Garhwa,Giridih,Godda,Gumla,Hazaribagh,Jamtara,Khunti,Kodarma,Latehar,Lohardaga,Pakaur,Palamu,Pashchimi Singhbhum,Purbi Singhbhum,Ramgarh,Ranchi,Sahibganj,Saraikela,Simdega'], ['Bagalakote,Bangalore Rural,Bangalore Urban,B.B.M.P East,B.B.M.P North,B.B.M.P South,B.B.M.P West,Belgaum,Bellary,Bidar,Bijapur,Chamarajanagar,Chikkaballapura,Chikmagalur,Chitradurga,Dakshina Kannada,Davanagere,Dharwad,Gadag,Gulbarga,Hassan,Haveri,HDMC,Kodagu,Kolar,Koppal,Mandya,Mysore,Raichur,Ramanagara,Shimoga,Tumkur,Udupi,Uttara Kannada,Yadgir'], ['Alappuzha,Ernakulam,Idukki,Kannur,Kasaragod,Kollam,Kottayam,Kozhikode,Malappuram,Palakkad,Pathanamthitta,Thiruvananthapuram,Thrissur,Wayanad'], ['Kargil,Leh,LehLadakh'], ['Agatti,Amini,Androth,Chetlat,Kadmath,Kalpeni,Kavaratti,Kiltan,Minicoy'], ['Agar Malwa,Alirajpur,Anuppur,Ashoknagar,Balaghat,Barwani,Betul,Bhind,Bhopal,Burhanpur,Chhatarpur,Chhindwara,Damoh,Datia,Dewas,Dhar,Dindori,Guna,Gwalior,Harda,Indore,Jabalpur,Jhabua,Katni,Khandwa,Khargone,Mandla,Mandsaur,Morena,Narmadapuram,Narsimhapur,Neemuch,Panna,Raisen,Rajgarh,Ratlam,Rewa,Sagar,Satna,Sehore,Seoni,Shahdol,Shajapur,Sheopur,Shivpuri,Sidhi,Sigrolli,Tikamgarh,Ujjain,Umaria,Vidisha'], ['Ahmadnagar,Akola,Amravati,Aurangabad,Beed,Bhandara,Bhiwandi Municipal Corporation (Thane Zone-5),Buldana,Chandrapur,Dhule,Gadchiroli,Gondiya,Greater Mumbai,Hingoli,Jalgaon,Jalna,Kalyan Tahashil (Thane Zone-8),Kolhapur,Latur,Mira Bhayander Municipal Corporation (Thane Zone-7),Nagpur,Nanded,Nandurbar,Nashik,Navi Mumbai Municipal Corporation (Thane Zone-2),Navi Mumbai Municipal Corporation (Thane Zone-3),Navi Mumbai Municipal Corporation (Thane Zone-4),Osmanabad,Palghar,Parbhani,Pune,Raigad,Ratnagiri,Sangli,Satara,Sindhudurg,Solapur,Thane Municipal Corporation (Thane Zone-1),Ulhasnagar & Ambarnath Tahashil (Thane Zone-9),Wardha,Washim,Yavatmal'], ['Bishnupur,CHANDEL,Churachandpur,Imphal East,Imphal West,JIRIBAM,KAKCHING,KAMJONG,KANGPOKPI,NONEY,PHERZAWL,SENAPATI,TAMENGLONG,TENGNOUPAL,Thoubal,UKHRUL'], ['East Garo Hills,East Jaintia Hills,East Khasi Hills,North Garo Hills,Ri Bhoi,South Garo Hills,South West Garo Hills,South West Khasi Hills,West Garo Hills,West Jaintia Hills,West Khasi Hills'], ['Aizawl East,Aizawl West,Champhai,Kolasib,Lawngtlai,Lunglei,Mamit,Saiha,Serchhip'], ['Dimapur,KIPHIRE,Kohima,LONGLENG,Mokokchung,Mon,PEREN,Phek,Tuensang,Wokha,Zunheboto'], ['ANGUL,BALASORE,BARAGARH,BERHAMPUR MUNICIPAL CORPORATION,BHADRAK,BHUBANESWAR MUNICIPAL CORPORATION,BOLANGIR,BOUDH,CUTTACK(EXCEPT MUNICIPAL CORPORATION),CUTTACK MUNICIPAL CORPORATION,DEOGARH,DHENKANAL,GAJAPATI,GANJAM(EXCEPT MUNICIPAL CORPORATION),JAGATSINGHPUR,JAJPUR,JHARSUGUDA,KALAHANDI,KANDHAMAL,KENDRAPARA,KEONJHAR,KHORDHA(EXCEPT MUNICIPAL CORPORATION),KORAPUT,MALKANGIRI,MAYURBHANJ,NAWARANGPUR,NAYAGARH,NUAPADA,PURI (EXCEPT MUNICIPALITY),PURI MUNICIPALITY,RAYAGADA,ROURKELA MUNICIPAL CORPORATION,SAMBALPUR(EXCEPT MUNICIPAL CORPORATION),SAMBALPUR MUNICIPAL CORPORATION,SONEPUR,SUNDARGARH(EXCEPT MUNICIPAL CORPORATION)'], ['Puducherry'], ['Amritsar,Barnala,Bathinda,Faridkot,Fatehgarh Sahib,Fazilka,Firozpur,Gurdaspur,Hoshiarpur,Jalandhar,Kapurthala,Ludhiana,Mansa,Moga,Mohali,Muktsar,Pathankot,Patiala,Rupnagar,Sangrur,Shaheed Bhagat Singh Nagar,Taran Taran'], ['Ajmer,Alwar,Banswara,Baran,Barmer,Bharatpur,Bhilwara,Bikaner,Bundi,Chittaurgarh,Churu,Dausa,Dhaulpur,Dungarpur,Hanumangarh,Jaipur,Jaisalmer,Jalor,Jhalawar,Jhunjhunun,Jodhpur,Karauli,Kota,Nagaur,Pali,Pratapgarh,Rajsamand,Sawai Madhopur,Shri Ganganagar,Sikar,Sirohi,Tonk,Udaipur'], ['East,Gangtok,North,South,West'], ['Ariyalur,Chennai,Coimbatore,Cuddalore,Dharmapuri,Dindigul,Erode,Kancheepuram,Kanyakumari,Karur,Krishnagiri,Madurai,Nagapattinam,Namakkal,Perambalur,Pudukkottai,Ramanathapuram,Salem,Sivaganga,Thanjavur,Theni,The Nilgiris,Thiruvallur,Thiruvarur,Thoothukkudi,Tiruchirappalli,Tirunelveli,Tirupur,Tiruvannamalai,Vellore,Viluppuram,Virudhunagar'], ['Adilabad,Badradri - Kothagudem,Cantonment-Sec-Bad,Hyderabad,Jagitial,Jangoan,Jayashanker-Bhoopalpally,Jogulamba - Gadwal,Kamareddy,Karimnagar,Khammam,Komarambheem,Mahabubabad,Mahbubnagar,Mancherial,Medak,Medchal-Malkajgiri,Nagar Kurnool,Nalgonda,Nirmal,Nizamabad,Peddapally,Rajanna,Rangareddi,Sangareddy,Siddipet,Suryapet,Vikarabad,Wanaparthy,Warangal,Yadadri - Bhongir'], ['Agartala Municipal Council,Dhalai,Gomati,Khowai,North Tripura,Sepahijala,South Tripura,Unakoti,West Tripura'], ['Almora,Bageshwar,Chamoli,Champawat,Dehradun,Hardwar,Nainital,Pauri Garhwal,Pithoragarh,Rudraprayag,Tehri Garhwal,Udham Singh Nagar,Uttarkashi'], ['Agra,Aligarh,Ambedkar Nagar,Amethi,Amroha,Auraiya,Ayodhya,Azamgarh,Baghpat,Bahraich,Ballia,Balrampur,Banda,Barabanki,Bareilly,Basti,Bijnor,Budaun,Bulandshahar,Chandauli,Chitrakoot,Deoria,Etah,Etawah,Farrukhabad,Fatehpur,Firozabad,Gautam Buddha Nagar,Ghaziabad,Ghazipur,Gonda,Gorakhpur,Hamirpur,Hapur,Hardoi,Hathras,Jalaun,Jaunpur,Jhansi,Kannauj,Kanpur Dehat,Kanpur Nagar,Kasganj,Kaushambi,Kheri,Kushinagar,Lakhimpur Khiri,Lalitpur,Lucknow,Mahoba,Mahrajganj,Mainpuri,Mathura,Mau,Meerut,Mirzapur,Moradabad,Muzaffarnagar,Pilibhit,Pratapgarh,Prayagraj,Rae Bareli,Rampur,Saharanpur,Sambhal,Sant Kabir Nagar,Sant Ravidas Nagar Bhadohi,Shahjahanpur,Shamali,Shrawasti,Siddharthnagar,Sitapur,Sonbhadra,Sultanpur,Unnao,Varanasi'], ['Alipurduar,Bankura,Basirhat Health District,Birbhum,Bishnupur Health District,Coochbehar,Dakshin Dinajpur,Darjeeling,DIAMOND HARBOUR HEALTH DISTRICT,Hooghly,Howrah,Jalpaiguri,JHARGRAM,Kalimpong,Kolkata,Maldah,Murshidabad,Nadia,NANDIGRAM HEALTH DISTRICT,North Twenty Four Parganas,PASCHIM BARDHAMAN,Paschim Mednipur,PURBA BARDHAMAN,Purba Medinipur,Puruliya,Rampurhat Health District,South Twenty Four Parganas,Uttar Dinajpur']]
"""
    # f = open(r"C:\Users\HP\PycharmProjects\SIHwhatsapp\Sub-Dist.txt", "a")
"""    for x in range(len(Dist)):
        f.write('[')
        partion = str(*Dist[x]).split(",")
        for y in partion:
            print(x,y)
            state = StAtr[x]
            State = Select(browser.find_element(By.CSS_SELECTOR,'select[formcontrolname="stateCode"]'))
            State.select_by_value(state)
            Dis = Select(browser.find_element(By.CSS_SELECTOR, 'select[formcontrolname="districtCode"]'))
            Dis.select_by_visible_text(y)
            time.sleep(2)
            ls=browser.find_elements(By.CSS_SELECTOR,'option[_ngcontent-c4]')
            word_ls = []
            for i in ls:
                word_ls.append(i.text)
            part=[]
            for i in range(len(word_ls)):
                print(word_ls[i], i)
                if word_ls[i] == 'Select Concern':
                    stop = i - 1
                    print("--------------------------------")
                    break
                if word_ls[i] == 'Select Sub-Disctrict':
                    start = i + 1
                    print("--------------------------------")
            print(start,stop)
            for i in range(start,stop+1):
                part.append(word_ls[i])
            f.write("[")
            for i in part:

                if i == part[-1]:
                    f.write('"%s"'%i)
                    f.write("]")
                    break
                f.write('"%s",'%(i))
        f.write("]")
    for i in ls:
        print(i.text)
    """
def getNews(Url="https://gadgets360.com/trends#pfrom=desktop-lhs-trending"):
    browser.get(Url)
    news = browser.find_elements(By.CSS_SELECTOR,'span[class="news_listing"]')
    # variable news is a WebElement ... This has to be processed ASAP and stored as string to avoid errors
    content=[]
    for i in range(10):
        content.append(news[i].text + "\n")
        print(content[i])
    return content
    time.sleep(2)
def whatsappSend(data,contact="amma"):
    browser.get("https://web.whatsapp.com/")
    browser.implicitly_wait(50)
    browser.find_element(By.CSS_SELECTOR,'div[role="textbox"]').send_keys(contact+"\n")
    TBox=browser.find_element(By.CSS_SELECTOR , 'p[class="selectable-text copyable-text"]')
    TBox.send_keys(data)

data=getNews()#"https://foscos.fssai.gov.in/consumergrievance/consumer/register-new-complaint")
whatsappSend(data)



"""
# To Make it Speak

engin=pyttsx3.init()
engin.setProperty("rate",160)
for i in content:
    engin.say(i)
    engin.runAndWait()
    time.sleep(2)
"""



