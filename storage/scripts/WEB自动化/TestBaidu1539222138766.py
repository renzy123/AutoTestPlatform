from selenium import webdriverimport unittestimport timefrom utils.consts import *class CollectProjects(unittest.TestCase):    def setUp(self):        self.driver = webdriver.Chrome(executable_path=os.path.join(DRIVER_PATH_MACOS, "chromedriver"))        # login        self.driver.get("http://100.64.15.43/zentao/user-login.html")        self.driver.implicitly_wait(10)        self.driver.minimize_window()        self.driver.find_element_by_id("loginPanel")        self.driver.find_element_by_id("account").send_keys("admin")        self.driver.find_element_by_name("password").send_keys("@Abcd1234")        self.driver.find_element_by_id("submit").click()        time.sleep(2)        self._get_projects()    def test_page_pre_order(self):        """获取预约界面的项目List"""        self.driver.get("http://100.64.15.43/zentao/resource-subscribe-admin.html")        datalist = self.driver.find_element_by_id("browsers")        options = datalist.find_elements_by_tag_name("option")        option_list = [element.get_property("value") for element in options][1:]        self._compare_list(self.in_progress_projects, option_list)    # def test_project_droplist(self):    #     """检查项目主页的下拉列表的数据是否正确"""    #     self.driver.get("http://100.64.15.43/zentao/project-index-no.html")    #     self.driver.find_element_by_id("currentItem").click()    #     # 获取下拉列表的    #     div_drop_down = self.driver.find_element_by_class_name("list-group")    #     rows = div_drop_down.find_elements_by_tag_name("a")    #     projects = [row.get_property("title") for row in rows]    #     all_project = self.in_progress_projects.copy()    #     all_project.extend(self.closed_projects)    #     self._compare_list(all_project,projects)    def _get_projects(self):        self.driver.get("http://100.64.15.43/zentao/project-all-all-0-order_desc-0-31-100-1.html")        project_table = self.driver.find_element_by_id("projectTableList")        # 找到所有的Row        rows_project = project_table.find_elements_by_tag_name("tr")        # 从Row中找到所有的进行中的项目的名称        _projects_in_progress = []        _project_closed = []        for row in rows_project:            status = row.find_element_by_class_name("status-text")            if str(status.text).rstrip() != "已关闭":                name = row.find_elements_by_tag_name("a")[0].text                _projects_in_progress.append(name)            else:                name = row.find_elements_by_tag_name("a")[0].text                _project_closed.append(name)        self.in_progress_projects = _projects_in_progress        self.closed_projects = _project_closed    def test_a_b(self):        self.assertTrue(1 + 2 == 3)    def _compare_list(self, list1: list, list2: list):        list1.sort()        list2.sort()        self.assertListEqual(list1, list2)    def tearDown(self):        self.driver.close()