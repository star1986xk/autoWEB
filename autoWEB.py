from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import requests
from mylogclass import MyLogClass

class DianXiaoMi():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.dianxiaomi.com/index.htm")
        self.log = MyLogClass()
        exampleInputName = self.wait.until(EC.presence_of_element_located((By.ID, "exampleInputName")))
        exampleInputName.send_keys('caohongjing123')
        exampleInputPassword = self.wait.until(EC.presence_of_element_located((By.ID, "exampleInputPassword")))
        exampleInputPassword.send_keys('Caohongjing334')

    # 关闭3个弹窗
    def close3(self):
        try:
            close_btn = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="myModal"]//div[@class="modal-footer"]/button')))
            close_btn.click()
        except Exception as e:
            print(e)
        time.sleep(1)
        try:
            close_btn = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="myModal"]//div[@class="modal-footer"]/button')))
            close_btn.click()
        except Exception as e:
            print(e)
        time.sleep(1)
        try:
            self.driver.execute_script("setUserMessageNoShowDays('597666', 0);")
        except Exception as e:
            print(e)
        time.sleep(1)
        try:
            close_btn = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="theNewestModalLabel"]//div[@class="modal-footer"]/button')))
            close_btn.click()
        except Exception as e:
            print(e)
        time.sleep(1)
        try:
            close_btn = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="theNewestModalLabel"]//div[@class="modal-footer"]/button')))
            close_btn.click()
        except Exception as e:
            print(e)
        time.sleep(1)
        try:
            close_btn = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="theNewestModalLabel"]//div[@class="modal-footer"]/button')))
            close_btn.click()
        except Exception as e:
            print(e)
        time.sleep(1)

    def getTime(self):
        t = requests.get('http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp').json()['data']['t']
        timeArray = time.localtime(int(t[:-3]))
        self.log.logger.info(str(timeArray))
        return timeArray

    def run1(self):
        # 点订单处理连接
        try:
            tabOrder = self.wait.until(EC.presence_of_element_located((By.XPATH, '//li[@id="tabOrder"]/a')))
            tabOrder.click()
            self.log.logger.info('订单处理')
        except Exception as e:
            self.log.logger.warning('订单处理')
        time.sleep(3)
        # 点同步订单按钮
        try:
            self.driver.execute_script("return syncOrder();")
            self.log.logger.info('同步订单')
        except Exception as e:
            self.log.logger.warning('同步订单')
        # 等待20分钟
        time.sleep(60*20)
        # 点关闭按钮
        try:
            guanbi = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="syncFromWishModal"]//button[contains(text(), "关闭")]')))
            guanbi.click()
            self.log.logger.info('同步订单关闭')
        except Exception as e:
            self.log.logger.warning('同步订单关闭')
        time.sleep(3)
        # 点待处理按钮
        try:
            daichuli = self.wait.until(EC.presence_of_element_located((By.ID, 'm101')))
            daichuli.click()
            self.log.logger.info('待处理')
        except Exception as e:
            self.log.logger.warning('待处理')
        time.sleep(3)
        #点可合并
        try:
            self.driver.execute_script("return getMergeOrderList(1,this);")
            self.log.logger.info('可合并')
        except Exception as e:
            self.log.logger.warning('可合并')
        time.sleep(3)
        # 点下拉300条按钮
        try:
            xuanxiang = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="dxmBody"]//select[@name="pageselct"]')))
            Select(xuanxiang).select_by_value('300')
            self.log.logger.info('可合并-300条')
        except Exception as e:
            self.log.logger.warning('可合并-300条')
        time.sleep(3)
        # 点全选按钮
        try:
            quanxuan = self.wait.until(EC.presence_of_element_located((By.XPATH, '//table[@id="orderListTable"]//th/input')))
            quanxuan.click()
            self.log.logger.info('可合并-全选')
        except Exception as e:
            self.log.logger.warning('可合并-全选')
        time.sleep(3)
        # 批量合并
        try:
            self.driver.execute_script('return batchMerge();')
            self.log.logger.info('批量合并')
        except Exception as e:
            self.log.logger.warning('批量合并')
        time.sleep(3)
        # 批量合并-单选
        try:
            danxuan = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="batchMergeConfigModal"]/div/div/div/div[2]//input')))
            danxuan.click()
            self.log.logger.info('批量合并-单选')
        except Exception as e:
            self.log.logger.warning('批量合并-单选')
        time.sleep(3)
        # 点弹窗确定按钮
        try:
            queding = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="batchMergeConfigModal"]//button[contains(text(), "确认")]')))
            queding.click()
            self.log.logger.info('批量合并-确定')
        except Exception as e:
            self.log.logger.warning('批量合并-确定')
        time.sleep(5)
        # 点待处理按钮
        try:
            daichuli = self.wait.until(EC.presence_of_element_located((By.ID, 'm101')))
            daichuli.click()
            self.log.logger.info('待处理')
        except Exception as e:
            self.log.logger.warning('待处理')
        time.sleep(3)
        # 点刷新规则按钮
        try:
            shuaxin = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "刷新规则")]')))
            shuaxin.click()
            self.log.logger.info('刷新规则')
        except Exception as e:
            self.log.logger.warning('刷新规则')
        time.sleep(3)
        # 选择单选框(待审核中)
        try:
            danxuan = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="approvedOrderRefreshRule"]//tr[1]//input')))
            danxuan.click()
            self.log.logger.info('刷新规则-选择单选框')
        except Exception as e:
            self.log.logger.warning('刷新规则-选择单选框')
        time.sleep(3)
        # 点弹窗确定按钮
        try:
            queding = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="approvedOrderRefreshRule"]//button[contains(text(), "确定")]')))
            queding.click()
            self.log.logger.info('刷新规则-确定')
        except Exception as e:
            self.log.logger.warning('刷新规则-确定')
        # 等待15秒
        time.sleep(15)
        # 点弹窗关闭按钮
        try:
            guanbi = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="refreshOrderRuleModal"]//button[contains(text(), "关闭")]')))
            guanbi.click()
        except Exception as e:
            print(e)
            pass
        time.sleep(3)
        # 点待处理按钮
        try:
            daichuli = self.wait.until(EC.presence_of_element_located((By.ID, 'm101')))
            daichuli.click()
            self.log.logger.info('待处理')
        except Exception as e:
            self.log.logger.warning('待处理')
        time.sleep(3)
        # 点全选按钮
        try:
            quanxuan = self.wait.until(EC.presence_of_element_located((By.XPATH, '//table[@id="orderListTable"]//th/input')))
            quanxuan.click()
            self.log.logger.info('待处理-全选')
        except Exception as e:
            self.log.logger.warning('待处理-全选')
        time.sleep(3)
        # 点所有条目
        try:
            quanxuan = self.wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@id="showSelCheckboxNum"]/td/span/span/span//a')))
            quanxuan.click()
            # self.driver.execute_script("return resultNumRange(this);")
            self.log.logger.info('点所有条目')
        except Exception as e:
            self.log.logger.warning('点所有条目')
        time.sleep(3)
        # 点申请运单号按钮
        try:
            self.driver.execute_script('return batchMoveProcessed();')
            self.log.logger.info('申请运单号')
        except Exception as e:
            self.log.logger.warning('申请运单号')
        time.sleep(5)
        # 点弹窗关闭按钮
        try:
            guanbi = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="batchOperateRetModal"]/div/div/div[3]/button')))
            guanbi.click()
            self.log.logger.info('申请运单号-关闭')
        except Exception as e:
            self.log.logger.warning('申请运单号-关闭')
        time.sleep(60*10)

    def run2(self,chongdanhaoTime):
        # 点订单处理连接
        try:
            tabOrder = self.wait.until(EC.presence_of_element_located((By.XPATH, '//li[@id="tabOrder"]/a')))
            tabOrder.click()
            self.log.logger.info('订单处理')
        except Exception as e:
            self.log.logger.warning('订单处理')
        time.sleep(1)
        # 点自营仓库按钮
        try:
            ziying = self.wait.until(EC.presence_of_element_located((By.ID, 'm10201')))
            ziying.click()
            self.log.logger.info('自营仓库')
        except Exception as e:
            self.log.logger.warning('自营仓库')
        time.sleep(1)
        # 点申请失败按钮
        try:
            shibai = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="dxmBody"]/div/div/ul/li[2]')))
            shibai.click()
            self.log.logger.info('申请失败')
        except Exception as e:
            self.log.logger.warning('申请失败')
        time.sleep(1)
        # 点重新获得单号按钮
        try:
            self.driver.execute_script("return batchReApplyTrackNum(0);")
            self.log.logger.info('重新获得单号')
        except Exception as e:
            self.log.logger.warning('重新获得单号')
        # 等待5分钟
        time.sleep(60*chongdanhaoTime)
        # 点弹窗关闭按钮
        try:
            guanbi = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="syncFromAutoReApplyModal"]//button[contains(text(), "关闭")]')))
            guanbi.click()
            self.log.logger.info('重新获得单号-关闭')
        except Exception as e:
            self.log.logger.warning('重新获得单号-关闭')
        time.sleep(3)
        # 再来一次
        # 点申请失败按钮
        try:
            shibai = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="dxmBody"]/div/div/ul/li[2]')))
            shibai.click()
            self.log.logger.info('申请失败')
        except Exception as e:
            self.log.logger.warning('申请失败')
        time.sleep(3)
        # 点重新获得单号按钮
        try:
            self.driver.execute_script("return batchReApplyTrackNum(0);")
            self.log.logger.info('重新获得单号')
        except Exception as e:
            self.log.logger.warning('重新获得单号')
        # 等待5分钟
        time.sleep(60*chongdanhaoTime)
        # 点弹窗关闭按钮
        try:
            guanbi = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="syncFromAutoReApplyModal"]//button[contains(text(), "关闭")]')))
            guanbi.click()
            self.log.logger.info('重新获得单号-关闭')
        except Exception as e:
            self.log.logger.warning('重新获得单号-关闭')
        time.sleep(3)
        # 点申请成功按钮
        try:
            chenggong = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="dxmBody"]/div/div/ul/li[1]')))
            chenggong.click()
            self.log.logger.info('申请成功')
        except Exception as e:
            self.log.logger.warning('申请成功')
        time.sleep(3)
        # 点下拉300条按钮
        try:
            xuanxiang = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="dxmBody"]//select[@name="pageselct"]')))
            Select(xuanxiang).select_by_value('300')
            self.log.logger.info('下拉-300条')
        except Exception as e:
            self.log.logger.warning('下拉-300条')
        time.sleep(3)
        # 点全选按钮
        try:
            quanxuan = self.wait.until(EC.presence_of_element_located((By.XPATH, '//table[@id="orderListTable"]//th/input')))
            quanxuan.click()
            self.log.logger.info('申请成功-全选')
        except Exception as e:
            self.log.logger.warning('申请成功-全选')
        time.sleep(3)
        # 点虚拟发货按钮
        try:
            self.driver.execute_script("return batchCommitPlatform();")
            self.log.logger.info('虚拟发货')
        except Exception as e:
            self.log.logger.warning('虚拟发货')
        time.sleep(3)
        # 点确定按钮
        try:
            queding = self.wait.until(EC.presence_of_element_located((By.ID, 'dialog_btn_enter')))
            queding.click()
            self.log.logger.info('虚拟发货-确定')
        except Exception as e:
            self.log.logger.warning('虚拟发货-确定')
        # 等10分钟
        time.sleep(60*10)
        # 点关闭按钮
        try:
            guanbi = self.wait.until(EC.presence_of_element_located((By.ID, 'batchOperatorBtn2')))
            guanbi.click()
            self.log.logger.info('虚拟发货-关闭')
        except Exception as e:
            self.log.logger.warning('虚拟发货-关闭')
        time.sleep(3)
        # 点全选按钮
        try:
            quanxuan = self.wait.until(EC.presence_of_element_located((By.XPATH, '//table[@id="orderListTable"]//th/input')))
            quanxuan.click()
            self.log.logger.info('申请成功-全选')
        except Exception as e:
            self.log.logger.warning('申请成功-全选')
        time.sleep(3)
        # 点移入待打单按钮
        try:
            daida = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="allClassification"]/div/button[contains(text(), "移入待打单")]')))
            daida.click()
            self.log.logger.info('移入待打单')
        except Exception as e:
            self.log.logger.warning('移入待打单')
        time.sleep(3)
        # 点单选按钮
        try:
            danxuan = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="fieldType1"]')))
            danxuan.click()
            self.log.logger.info('移入待打单-单选')
        except Exception as e:
            self.log.logger.warning('移入待打单-单选')
        time.sleep(3)
        # 点确定按钮
        try:
            queding = self.wait.until(EC.presence_of_element_located((By.ID, 'batchMoveAllocatedConfirmBtn')))
            queding.click()
            self.log.logger.info('移入待打单-确定')
        except Exception as e:
            self.log.logger.warning('移入待打单-确定')
        time.sleep(3)

if __name__ == '__main__':
    OBJ = DianXiaoMi()
    while True:
        OBJ.close3()
        nowTime = OBJ.getTime()
        if nowTime.tm_hour==7 and nowTime.tm_min==5:
            OBJ.run1()
            OBJ.run2(5)
        elif nowTime.tm_hour==20 and nowTime.tm_min==5:
            OBJ.run1()
            OBJ.run2(5)
        elif nowTime.tm_hour==23 and nowTime.tm_min==59:
            sec = (59-nowTime.tm_sec)
            time.sleep(sec)
            OBJ.run2(15)
        time.sleep(20)
        OBJ.driver.refresh()
