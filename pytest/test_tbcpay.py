# საჭირო იმპორტები
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys

# დრაივერის მისამართი, ბრაუზერის გახსნა, მისამართზე შესვლა, ფანჯრის გადიდება
chrome = "C:\\bin\chromedriver.exe"
driver = webdriver.Chrome(chrome)
address = "https://tbcpay.ge/"
driver.get(address)
driver.maximize_window()
driver.save_screenshot('home_page.png')
time.sleep(3)

'''     პირველი პუნქტი     '''


# "სერვისები"-ს არსებობის შემოწმება
def test_head_service():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/header/section/div[2]/div/nav/a[2]')
        allure.attach(driver.get_screenshot_as_png(), name="Service", attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "გადარიცხვები"-ს არსებობის შემოწმება
def test_head_transfers():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/header/section/div[2]/div/nav/a[3]')
        allure.attach(driver.get_screenshot_as_png(), name="Transfers",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "ბიზნესისთვის"-ის არსებობის შემოწმება
def test_head_forbusiness():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/header/section/div[2]/div/nav/a[4]')
        allure.attach(driver.get_screenshot_as_png(), name="ForBusiness",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "გადაიხადე უცხოეთიდან"-ის არსებობის შემოწმება
def test_head_foreignpayments():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/header/section/div[2]/div/nav/a[5]')
        allure.attach(driver.get_screenshot_as_png(), name="ForeignPayments",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# სერვისების ნავიგაციის შემოწმება

# "პოპულარული სერვისები"-ს არსებობის შემოწმება
def test_nav_popularservices():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[1]/a')
        allure.attach(driver.get_screenshot_as_png(), name="PopularServices",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "მობილური კავშირი"-ს არსებობის შემოწმება
def test_nav_mobileconn():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[2]/a')
        allure.attach(driver.get_screenshot_as_png(), name="MobileConn",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "ბანკები დაზღვევა მიკროსაფინანსო"-ს არსებობის შემოწმება
def test_nav_banks():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[3]/a')
        allure.attach(driver.get_screenshot_as_png(), name="Banks",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "ტოტალიზატორები კაზინო ლატარია"-ს არსებობის შემოწმება
def test_nav_casinos():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[4]/a')
        allure.attach(driver.get_screenshot_as_png(), name="Casinos",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "ინტერნეტი ტელეფონი ტელევიზია"-ს არსებობის შემოწმება
def test_nav_internet():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[5]/a')
        allure.attach(driver.get_screenshot_as_png(), name="Internet",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "კომუნალური გადახდები"-ს არსებობის შემოწმება
def test_nav_taxes():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[6]/a')
        allure.attach(driver.get_screenshot_as_png(), name="Taxes",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "ტრანსპორტი"-ს არსებობის შემოწმება
def test_nav_transport():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[7]/a')
        allure.attach(driver.get_screenshot_as_png(), name="Transport",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "სახელმწიფო სერვისების"-ს არსებობის შემოწმება
def test_nav_stateserv():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[8]/a')
        allure.attach(driver.get_screenshot_as_png(), name="StateServ",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


# "სხვადასხვა"-ს არსებობის შემოწმება
def test_nav_other():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[9]/a')
        allure.attach(driver.get_screenshot_as_png(), name="Other",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


'''     მეორე პუნქტი     '''


# "მობილური"-ს ძიება და შემდეგ შედეგის შემოწმება
def test_search_mobile():
    time.sleep(3)
    # ძიება საძიებო ველში
    searchinput = driver.find_element_by_name('searchWord')
    searchinput.send_keys("მობილური")
    allure.attach(driver.get_screenshot_as_png(), name="MobileFillIn",
                  attachment_type=AttachmentType.PNG)
    # შედეგის შემოწმება
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/div[1]/div/div[2]/div/div/div/form/button')
    searchinput.send_keys(Keys.RETURN)
    time.sleep(3)
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section/table/tbody/tr[2]/td[2]')
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="MobileSearch",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


'''     მესამე პუნქტი     '''


# ტექსტზე დაჭერის შემდეგ შესაყვანი ველისა და ღილაკის შემოწმება
def test_mobilebalance():
    # ტექსტზე დაჭერა
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/section/table/tbody/tr[2]/td[2]').click()
    time.sleep(3)
    # ღილაკის და ველის შემოწმება
    try:
        driver.find_element_by_name("1213-abonentCode")
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div/div[2]/form/button')
        allure.attach(driver.get_screenshot_as_png(), name="MobileSearch2",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


'''     მეოთხე პუნქტი     '''


# ველის შევსება ტელეფონის ნომრით
def test_numberdeposit():
    try:
        driver.find_element_by_name("1213-abonentCode").send_keys("555122334")
        allure.attach(driver.get_screenshot_as_png(), name="MobileSearch3",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


'''     მეხუთე პუნქტი     '''


# ძიება და ველების არსებობის შემოწმება ჩამონათვალში
def test_number():
    driver.find_element_by_name("1213-abonentCode").send_keys(Keys.RETURN)
    time.sleep(6)
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[2]/div[2]/div/div/label').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[2]/div[2]/div/div/div/a[2]')
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[2]/div[2]/div/div/div/a[3]')
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[2]/div[2]/div/div/div/a[4]')
        allure.attach(driver.get_screenshot_as_png(), name="MobileSearch4",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


'''     მეექვსე პუნქტი     '''

# ტექსტების და ღილაკის შემოწმება
def test_checkmoreten():
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[2]/div[2]/div/div/div/a[4]').click()
    time.sleep(3)
    try:
        # დავალიანება
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[1]/small/span')
        # 10.00 c
        driver.find_element_by_xpath(
            '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[1]/p')
        # თანხის ოდენობა c
        driver.find_element_by_xpath(
            '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[2]/small')
        # 10
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[2]/div/input')
        # საკომისიო
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[3]/div[1]/button/small/span')
        # 0.12c
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[3]/div[2]/button')
        # ჯამში გადასახდელი
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[2]/div/div[1]/small/span')
        # 10.12 c
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[2]/div/div[1]/b')
        # გადახდა
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/button[2]')

        allure.attach(driver.get_screenshot_as_png(), name="CheckMorePackage",
                      attachment_type=AttachmentType.PNG)
    except NoSuchElementException:
        raise NoSuchElementException


'''     მეშვიდე პუნქტი     '''

def test_pay():
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/button[2]').click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="LastScreen",
                  attachment_type=AttachmentType.PNG)

    if "ecommerce.ufc.ge" not in driver.current_url:
        raise Exception
    driver.quit()
