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
        exampleInputName = self.wait.until(EC.element_to_be_clickable((By.ID, "exampleInputName")))
        exampleInputName.send_keys('caohongjing123')
        exampleInputPassword = self.wait.until(EC.element_to_be_clickable((By.ID, "exampleInputPassword")))
        exampleInputPassword.send_keys('Caohongjing001')

    # 关闭3个弹窗
    def close3(self):
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//div[@id="myModal"]//div[@class="modal-footer"]/button')))
            close_btn.click()
        except Exception as e:
            print(e)
        time.sleep(1)
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//div[@id="myModal"]//div[@class="modal-footer"]/button')))
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
            close_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//div[@id="theNewestModalLabel"]//div[@class="modal-footer"]/button')))
            close_btn.click()
        except Exception as e:
            print(e)
        time.sleep(1)
        try:
            close_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//div[@id="theNewestModalLabel"]//div[@class="modal-footer"]/button')))
            close_btn.click()
        except Exception as e:
            print(e)
        time.sleep(1)
        try:
            close_btn = self.wait.until(EC.element_to_be_clickable(
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

    # 订单处理
    def dingdanchuli(self, count):
        if count < 3:
            try:
                tabOrder = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="tabOrder"]/a')))
                tabOrder.click()
                self.log.logger.info('订单处理')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.dingdanchuli(count)
        else:
            self.log.logger.warning('订单处理')

    #同步订单
    def tongbudingdan(self,count):
        if count < 3:
            try:
                self.driver.execute_script("return syncOrder();")
                self.log.logger.info('同步订单')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.tongbudingdan(count)
        else:
            self.log.logger.warning('同步订单')

    #同步订单关闭
    def tongbudingdan_guanbi(self,count):
        if count < 3:
            try:
                guanbi = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="syncFromWishModal"]//div[@class="modal-header"]/button')))
                guanbi.click()
                self.log.logger.info('同步订单关闭')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.tongbudingdan_guanbi(count)
        else:
            self.log.logger.warning('同步订单关闭')

    #待处理
    def daichuli(self,count):
        if count < 3:
            try:
                daichuli = self.wait.until(EC.element_to_be_clickable((By.ID, 'm101')))
                daichuli.click()
                self.log.logger.info('待处理')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.daichuli(count)
        else:
            self.log.logger.warning('待处理')

    #合并
    def hebing(self,count):
        if count < 3:
            try:
                hebing = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@id="dxmBody"]/div//ul/li[3]/a')))
                hebing.click()
                self.log.logger.info('可合并')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.hebing(count)
        else:
            self.log.logger.warning('可合并')

    #合并300
    def hebing300(self,count):
        if count < 3:
            try:
                xuanxiang = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@id="dxmBody"]//select[@name="pageselct"]')))
                Select(xuanxiang).select_by_value('300')
                self.log.logger.info('可合并-300条')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.hebing300(count)
        else:
            self.log.logger.warning('可合并-300条')

    #合并全选
    def hebingquanxuan(self,count):
        if count < 3:
            try:
                quanxuan = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//table[@id="orderListTable"]//th/input')))
                quanxuan.click()
                self.log.logger.info('可合并-全选')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.hebingquanxuan(count)
        else:
            self.log.logger.warning('可合并-全选')

    #批量合并
    def pilianghebing(self,count):
        if count < 3:
            try:
                self.driver.execute_script('return batchMerge();')
                self.log.logger.info('批量合并')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.pilianghebing(count)
        else:
            self.log.logger.warning('批量合并')

    #批量合并-单选
    def pilianghebing_danxuan(self,count):
        if count < 3:
            try:
                danxuan = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="batchMergeConfigModal"]/div/div/div/div[2]//input')))
                danxuan.click()
                self.log.logger.info('批量合并-单选')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.pilianghebing_danxuan(count)
        else:
            self.log.logger.warning('批量合并-单选')

    #批量合并-确认
    def pilianghebing_queren(self,count):
        if count < 3:
            try:
                queding = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="batchMergeConfigModal"]//button[@id="batchMergeConform"]')))
                queding.click()
                self.log.logger.info('批量合并-确定')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.pilianghebing_queren(count)
        else:
            self.log.logger.warning('批量合并-确定')

    #刷新规则
    def shuaxinguize(self,count):
        if count < 3:
            try:
                shuaxin = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="allClassification"]//button[contains(text(), "刷新规则")]')))
                shuaxin.click()
                self.log.logger.info('刷新规则')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.shuaxinguize(count)
        else:
            self.log.logger.warning('刷新规则')
    
    #刷新规则单选
    def shuaxinguize_danxuan(self,count):
        if count < 3:
            try:
                danxuan = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@id="approvedOrderRefreshRule"]//tr[1]//input')))
                danxuan.click()
                self.log.logger.info('刷新规则-选择单选框')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.shuaxinguize_danxuan(count)
        else:
            self.log.logger.warning('刷新规则-选择单选框')

    #刷新规则确定
    def shuaxinguize_queding(self,count):
        if count < 3:
            try:
                queding = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="approvedOrderRefreshRule"]//button[contains(text(), "确定")]')))
                queding.click()
                self.log.logger.info('刷新规则-确定')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.shuaxinguize_queding(count)
        else:
            self.log.logger.warning('刷新规则-确定')

    #刷新规则关闭
    def shuaxinguize_guanbi(self,count):
        if count < 3:
            try:
                guanbi = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="refreshOrderRuleModal"]//div[@class="modal-header"]/button')))
                guanbi.click()
                self.log.logger.info('刷新规则-关闭')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.shuaxinguize_guanbi(count)
        else:
            self.log.logger.warning('刷新规则-关闭')

    #待处理_下拉
    def daichuli_xiala(self,count):
        if count < 3:
            try:
                xuanxiang = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//ul[@id="upPage"]//select[@name="pageselct"]')))
                Select(xuanxiang).select_by_value('300')
                self.log.logger.info('待处理-300条')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.daichuli_xiala(count)
        else:
            self.log.logger.warning('待处理-300条')

    #待处理_全选
    def daichuli_quanxuan(self,count):
        if count < 3:
            try:
                quanxuan = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//table[@id="orderListTable"]//th/input')))
                quanxuan.click()
                self.log.logger.info('待处理-全选')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.daichuli_quanxuan(count)
        else:
            self.log.logger.warning('待处理-全选')

    #所有条目
    def suoyoutiaomu(self,count):
        if count < 3:
            try:
                quanxuan = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//tr[@id="showSelCheckboxNum"]/td/span/span/span//a')))
                quanxuan.click()
                self.log.logger.info('点所有条目')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.suoyoutiaomu(count)
        else:
            self.log.logger.warning('点所有条目')

    #申请运单号
    def shenqingyundanhao(self,count):
        if count < 3:
            try:
                self.driver.execute_script('return batchMoveProcessed();')
                self.log.logger.info('申请运单号')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.shenqingyundanhao(count)
        else:
            self.log.logger.warning('申请运单号')

    #弹窗_关闭
    def tanchuang_guanbi(self,count):
        if count < 3:
            try:
                guanbi = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="batchOperateRetModal"]//div[@class="modal-header"]/button')))
                guanbi.click()
                self.log.logger.info('关闭窗口')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.tanchuang_guanbi(count)
        else:
            self.log.logger.warning('关闭窗口')

    #自营仓库
    def ziyingcangku(self,count):
        if count < 3:
            try:
                ziying = self.wait.until(EC.element_to_be_clickable((By.ID, 'm10201')))
                ziying.click()
                self.log.logger.info('自营仓库')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.ziyingcangku(count)
        else:
            self.log.logger.warning('自营仓库')

    #申请失败
    def shenqingshibai(self,count):
        if count < 3:
            try:
                shibai = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@id="dxmBody"]/div/div/ul/li[2]/a')))
                shibai.click()
                self.log.logger.info('申请失败')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.shenqingshibai(count)
        else:
            self.log.logger.warning('申请失败')

    #重获订单号
    def conghuodanhao(self,count):
        if count < 3:
            try:
                self.driver.execute_script("return batchReApplyTrackNum(0);")
                self.log.logger.info('重新获得订单号')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.conghuodanhao(count)
        else:
            self.log.logger.warning('重新获得订单号')

    #重获订单号_关闭
    def conghuodanhao_guanbi(self,count):
        if count < 3:
            try:
                guanbi = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="syncFromAutoReApplyModal"]//div[@class="modal-header"]/button')))
                guanbi.click()
                self.log.logger.info('重新获得单号-关闭')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.conghuodanhao_guanbi(count)
        else:
            self.log.logger.warning('重新获得单号-关闭')

    #申请成功
    def shenqingchenggong(self,count):
        if count < 3:
            try:
                chenggong = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@id="dxmBody"]/div/div/ul/li[1]/a')))
                chenggong.click()
                self.log.logger.info('申请成功')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.shenqingchenggong(count)
        else:
            self.log.logger.warning('申请成功')

    #申请成功_下拉
    def shenqingchenggong_xiala(self,count):
        if count < 3:
            try:
                xuanxiang = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@id="dxmBody"]//select[@name="pageselct"]')))
                Select(xuanxiang).select_by_value('300')
                self.log.logger.info('申请成功-下拉')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.shenqingchenggong_xiala(count)
        else:
            self.log.logger.warning('申请成功-下拉')

    #申请成功_全选
    def shenqingchenggong_quanxuan(self,count):
        if count < 3:
            try:
                quanxuan = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//table[@id="orderListTable"]//th/input')))
                quanxuan.click()
                self.log.logger.info('申请成功-全选')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.shenqingchenggong_quanxuan(count)
        else:
            self.log.logger.warning('申请成功-全选')

    #虚拟发货
    def xunifahuo(self,count):
        if count < 3:
            try:
                self.driver.execute_script("return batchCommitPlatform();")
                self.log.logger.info('虚拟发货')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.xunifahuo(count)
        else:
            self.log.logger.warning('虚拟发货')

    #虚拟发货_确定
    def xunifahuo_queding(self,count):
        if count < 3:
            try:
                queding = self.wait.until(EC.element_to_be_clickable((By.ID, 'dialog_btn_enter')))
                queding.click()
                self.log.logger.info('虚拟发货-确定')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.xunifahuo_queding(count)
        else:
            self.log.logger.warning('虚拟发货-确定')

    #移入待打单
    def daidadan(self,count):
        if count < 3:
            try:
                daida = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="allClassification"]/div/button[contains(text(), "移入待打单")]')))
                daida.click()
                self.log.logger.info('移入待打单')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.daidadan(count)
        else:
            self.log.logger.warning('移入待打单')

    #待打单_单选
    def daidadan_danxuan(self,count):
        if count < 3:
            try:
                danxuan = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="fieldType1"]')))
                danxuan.click()
                self.log.logger.info('移入待打单-单选')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.daidadan_danxuan(count)
        else:
            self.log.logger.warning('移入待打单-单选')

    #待打单_确定
    def daidadan_queding(self,count):
        if count < 3:
            try:
                queding = self.wait.until(EC.element_to_be_clickable((By.ID, 'batchMoveAllocatedConfirmBtn')))
                queding.click()
                self.log.logger.info('移入待打单-确定')
            except Exception as e:
                count += 1
                time.sleep(1)
                self.daidadan_queding(count)
        else:
            self.log.logger.warning('移入待打单-确定')

    def run1(self):
        # 点订单处理连接
        self.dingdanchuli(0)
        # 点同步订单按钮
        self.tongbudingdan(0)
        # 等待20分钟
        time.sleep(60*20)
        # 点关闭按钮
        self.tongbudingdan_guanbi(0)
        # 点待处理按钮
        self.daichuli(0)
        # 点可合并
        self.hebing(0)
        # 点下拉300条按钮
        self.hebing300(0)
        # 点全选按钮
        self.hebingquanxuan(0)
        # 批量合并
        self.pilianghebing(0)
        # 批量合并-单选
        self.pilianghebing_danxuan(0)
        # 点弹窗确定按钮
        self.pilianghebing_queren(0)
        time.sleep(5)
        # 点待处理按钮
        self.daichuli(0)
        # 点刷新规则按钮
        self.shuaxinguize(0)
        # 刷新规则_单选框(待审核中)
        self.shuaxinguize_danxuan(0)
        # 刷新规则_确定
        self.shuaxinguize_queding(0)
        # 等待15秒
        time.sleep(15)
        # 刷新规则_关闭
        self.shuaxinguize_guanbi(0)
        # 点待处理按钮
        self.daichuli(0)
        # 待处理300条
        self.daichuli_xiala(0)
        # 点全选按钮
        self.daichuli_quanxuan(0)
        # 点申请运单号按钮
        self.shenqingyundanhao(0)
        time.sleep(5)
        # 点弹窗关闭按钮
        self.tanchuang_guanbi(0)
        time.sleep(60 * 10)

    def run2(self, chongdanhaoTime):
        # 点订单处理连接
        self.dingdanchuli(0)
        time.sleep(1)
        # 点自营仓库按钮
        self.ziyingcangku(0)
        time.sleep(1)
        # 点申请失败按钮
        self.shenqingshibai(0)
        time.sleep(1)
        # 点重新获得单号按钮
        self.conghuodanhao(0)
        # 等待5分钟
        time.sleep(60 * chongdanhaoTime)
        # 点弹窗关闭按钮
        self.conghuodanhao_guanbi(0)

        # 点申请失败按钮
        self.shenqingshibai(0)
        time.sleep(1)
        # 点重新获得单号按钮
        self.conghuodanhao(0)
        # 等待5分钟
        time.sleep(60 * chongdanhaoTime)
        # 点弹窗关闭按钮
        self.conghuodanhao_guanbi(0)

        # 点申请成功按钮
        self.shenqingchenggong(0)
        # 点下拉300条按钮
        self.shenqingchenggong_xiala(0)
        # 点全选按钮
        self.shenqingchenggong_quanxuan(0)
        # 点虚拟发货按钮
        self.xunifahuo(0)
        # 点确定按钮
        self.xunifahuo_queding(0)
        # 等10分钟
        time.sleep(60 * 10)
        # 点关闭按钮
        self.tanchuang_guanbi(0)
        # 点申请成功按钮
        self.shenqingchenggong(0)
        # 点全选按钮
        self.shenqingchenggong_quanxuan(0)
        # 点移入待打单按钮
        self.daidadan(0)
        # 点单选按钮
        self.daidadan_danxuan(0)
        # 点确定按钮
        self.daidadan_queding(0)
        time.sleep(10)
        # 点关闭按钮
        self.tanchuang_guanbi(0)

if __name__ == '__main__':
    OBJ = DianXiaoMi()
    while True:
        OBJ.close3()
        nowTime = OBJ.getTime()
        if nowTime.tm_hour == 1 and nowTime.tm_min == 5:
            OBJ.run1()
            OBJ.run2(5)
        elif nowTime.tm_hour == 7 and nowTime.tm_min == 5:
            OBJ.run1()
            OBJ.run2(5)
        elif nowTime.tm_hour == 20 and nowTime.tm_min == 5:
            OBJ.run1()
            OBJ.run2(5)
        elif nowTime.tm_hour == 23 and nowTime.tm_min == 59:
            sec = (55 - nowTime.tm_sec)
            time.sleep(sec)
            OBJ.run2(15)
        time.sleep(20)
        OBJ.driver.refresh()
