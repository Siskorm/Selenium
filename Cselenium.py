from asyncio.windows_events import NULL
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

PATH_DRIVER = r'C:/chromedriver.exe'

class ClassSelenium:
    driver = ""
    drive = ""
    data = {}
    def navegador(self,drive):
        self.drive = drive
        self.driver = webdriver.Chrome(executable_path=PATH_DRIVER)
        return self.driver
        pass
    def ventana(self,drive,url):
        drive.get(""+str(url)+"")
        pass



    def dimension_tabla(self,tr,th,drive):
        title = th.replace('"', "'")
        rowscolumns = tr.replace('"', "'")
        title2 = drive.find_elements(By.XPATH, ""+str(title)+"")
        rowscolumns2 = drive.find_elements(By.XPATH, ""+str(rowscolumns)+"")
        for t in range(len(title2)):
            # TODO() INSERTANDO LOS TITULOS DE CABECERA
            if len(title2[t].text) > 1:
                self.data[title2[t].text] = []
        for col in range(1, len(rowscolumns2) + 1):
            # TODO() LOS TITULOS ASIGNANDO ELEMENTO POR CAMPO EN SI 34 FILAS POR 10 CAMPOS
            for d in range(1, len(title2)):
                text = drive.find_element(By.XPATH,str(rowscolumns)+"[" + str(col) + "]/td[" + str(d) + "]").text
                if len(text) > 1:
                    self.data[title2[d - 1].text].append(text)
        return self.data
        pass





    def FindByAndAction(self, type, selector, action, value):
        element = NULL
        try:
            if type == 'xpath':
                element = self.driver.find_element(By.XPATH, selector)
            elif type == 'id':
                element = self.driver.find_element('id',selector)
            elif type == 'name':
                element = self.driver.find_element('name',selector)
        except NoSuchElementException:
            return False

        self.ElementAction(element, action, value)
        pass
    

    def Click(self, element):
        element.click()
        pass

    def WriteInput(self, element, value):
        element.click()
        time.sleep(.2)
        element.send_keys(value)
        pass

    def WriteSelect(self, element, value):
        element.select_by_visible_text(value)
        pass

    def Submit(self, element):
        element.submit()
        pass

    def MoveToElementAndClick(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()
        # element.move_to_element(element).click().perform()
        pass

    def DobleClick(self, element):
        ActionChains(self.driver).double_click(element).click().perform()
        pass

    def ReadTable(self, type_th,selector_th, type_tb,selector_tb):
        def FindBy(type, selector):
            element = NULL
            try:
                if type == 'xpath':
                    element = self.driver.find_elements(By.XPATH, selector)
                elif type == 'id':
                    element = self.driver.find_elements('id',selector)
                elif type == 'name':
                    element = self.driver.find_elements('name',selector)
            except NoSuchElementException:
                return False
                
            return element
            
        thead = FindBy(type_th,selector_th)
        tbody = FindBy(type_tb,selector_tb)
        for t in range(len(thead)):
            # TODO() INSERTANDO LOS TITULOS DE CABECERA
            if len(thead[t].text) > 1:
                self.data[thead[t].text] = []
        for col in range(1, len(tbody) + 1):
            # TODO() LOS TITULOS ASIGNANDO ELEMENTO POR CAMPO EN SI 34 FILAS POR 10 CAMPOS
            for d in range(1, len(thead)):
                text = self.driver.find_element(By.XPATH, selector_tb +"[" + str(col) + "]/td[" + str(d) + "]").text
                if len(text) > 1:
                    self.data[thead[d - 1].text].append(text)

        
        return self.data
        pass
    


    
    def ElementAction(self, element, action, value):
        if action == 'click':
            self.Click(element)
        elif action == 'write_input':
            self.WriteInput(element,value)
        elif action == 'write_select':
            self.WriteSelect(element,value)
        elif action == 'submit':
            self.Submit(element)
        elif action == 'move_to_element_and_click':
            self.MoveToElementAndClick(element)
        elif action == 'doble_click':
            self.DobleClick(element)
        pass

    

    

