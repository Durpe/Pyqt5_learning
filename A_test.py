# -*- coding: utf-8 -*-
from tkinter import Tk, Button, Entry,Label,StringVar, Checkbutton,IntVar
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font as tkFont
from os import getcwd, listdir, path, makedirs, getenv,popen
from shutil import copy, copytree, rmtree
import getpass
import pymysql
import winreg

# MDSV5版本号
VERSION = '1.0.2'


class Window(object):
    def __init__(self):
        self.application_window = Tk()
        self.application_window.wm_attributes('-topmost', 1)
        self.application_window.geometry("420x200+600+400")
        self.application_window.title("请选择需要配置的软件位置")
        # 读取host.txt的内容（路径）
        self.host = open(getcwd() + '/mdsv5installpath.cfg', 'r')
        self.host_path = self.host.read().strip('\n')
        self.host.close()
        self.application_window.iconbitmap('./logo.ico')
        self.software_box()


    # 返回当前用户正在使用版本的中望路径
    @property
    def zw_file(self):
        try:
            string = r'SOFTWARE\ZWSOFT\ZW3D\CurrentVersion'
            handle = winreg.OpenKey(winreg.HKEY_CURRENT_USER, string, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ))
            location, _type = winreg.QueryValueEx(handle, "ZW3DLocation")
            LOC = '/'.join(location.split('\\')[:-1])  # 中望的路径
            return LOC
        except:
            return ''

    # 返回creo最新版本
    @property
    def creo_version(self):
        version = []
        try:
            creo_root_path = listdir('D:/PTC/Creo 4.0/')
            for each in creo_root_path:
                if each[0].upper() == "M":
                    version.append(each.split("M")[1])
            max_index = max(enumerate(version))
            creo_version = 'M' + max_index[1]
            # 返回creo的版本
            return creo_version
        except:
            return ''


    def software_box(self):
        self.var_zw = IntVar()
        self.var_creo = IntVar()
        self.var1_catia = IntVar()
        self.check_zw = Checkbutton(self.application_window,text='中望',variable=self.var_zw)
        self.check_creo = Checkbutton(self.application_window,text='Creo',variable=self.var_creo)
        #self.check_catia = Checkbutton(self.application_window,text='Catia',variable=self.var1_catia)
        self.check_zw.grid(row=1, column=0, padx=10, pady=5, ipadx=10, ipady=5)
        self.check_creo.grid(row=2, column=0, padx=10, pady=5, ipadx=10, ipady=5)
        #self.check_catia.grid(row=3, column=0, padx=10, pady=5, ipadx=10, ipady=5)

        self.btn_zw = Button(self.application_window, text='选择路径', width=5,
                           command=lambda: self.get_address(name="中望", txt_box=self.txt_box1))
        # self.btn_zw = Button(self.application_window, text='选择路径', width=5,state='disabled')
        self.btn_zw.grid(row=1, column=2, padx=10, pady=5, ipadx=10, ipady=5)
        self.btn_creo = Button(self.application_window, text='选择路径', width=5,state='disabled')
        self.btn_creo.grid(row=2, column=2, padx=10, pady=5, ipadx=10, ipady=5)
        # self.btn2 = Button(self.application_window, text='CREO', width=10)
        # self.btn2.grid(row=2, column=1, padx=10, pady=5, ipadx=10, ipady=5)
        # catia取消
        # self.btn_catia = Button(self.application_window, text='选择路径', width=5,state='disabled')
        # self.btn_catia.grid(row=3, column=2, padx=10, pady=5, ipadx=10, ipady=5)

        # zw


        textVar_zw = StringVar()
        if self.zw_file != '':
            textVar_zw.set(self.zw_file)
        else:
            textVar_zw.set('未在本计算机找到中望的路径,请手动选择')
        self.txt_box1 = Entry(self.application_window, width=30,textvariable=textVar_zw)
        self.txt_box1.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        # Creo
        textVar_creo = StringVar()
        if self.creo_version != '':
            textVar_creo.set('D:/PTC/Creo 4.0/'+ self.creo_version +'/Common Files/x86e_win64/obj')
        else:
            textVar_creo.set('本机未安装Creo,无法配置Creo插件')
        self.txt_box2 = Entry(self.application_window, width=30, textvariable=textVar_creo, state='disabled')
        self.txt_box2.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        # Catia(取消)
        # textVar_catia = StringVar()
        # textVar_catia.set('C:/ProgramData/DassaultSystemes/CATEnv')
        # self.txt_box3 = Entry(self.application_window, width=30,textvariable = textVar_catia, state='disabled')
        # self.txt_box3.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        # self.btn4 = Button(self.application_window, text='确认', width=5, command=lambda: self.copy_file_ZW())
        # self.btn4.grid(row=1, column=3, padx=10, pady=5, ipadx=10, ipady=5)
        # self.btn5 = Button(self.application_window, text='确认', width=5,command=lambda: self.copy_file_CREO())
        # self.btn5.grid(row=2, column=3, padx=10, pady=5, ipadx=10, ipady=5)
        # self.btn6 = Button(self.application_window, text='确认', width=5, command=lambda: self.copy_file_Catia())
        # self.btn6.grid(row=3, column=3, padx=10, pady=5, ipadx=10, ipady=5)

        ft = tkFont.Font(size=12)
        self.confirm = Button(self.application_window, text='确认', width=5,height=1,font=ft,command=lambda: self.copy_confirm())
        self.confirm.grid(row=4, column=1,pady=40)
        # self.close = Button(self.application_window, text='关闭', width=5,height=1,font=ft)
        # self.close.grid(row=4,column=2)
        self.application_window.mainloop()

    # 地址选择
    def get_address(self, name, txt_box):
        txt_box.delete(0, 'end')
        response = filedialog.askdirectory(parent=self.application_window, initialdir="C:", title="请选择%s的安装路径" % name)
        txt_box.insert(0, response)


    # 复制ZW的api和qt文件
    def copy_file_ZW(self):
        self.user_name = getpass.getuser()  # 获取当前用户名
        # api的原地址
        file_path = self.host_path + '/apilibs/zwmds.dll'
        # Qt的内容
        file_names = ["Qt5Gui.dll", "Qt5Core.dll", "Qt5Sql.dll", "Qt5Svg.dll", "Qt5Widgets.dll", "libmysql.dll"]
        try:
            for each in popen('tasklist'):
                if each.lower().find('zw3d') >= 0:
                    self.zw_in_process = '检测到中望未关闭,请关闭中望后重新尝试'
                    self.zw_log = '中望MDS插件未配置'
                    #messagebox.showerror('错误', e)
                    messagebox.showerror('信息', self.zw_in_process)
                    return
            # 源api地址里的dll文件
            #file_name = listdir(file_path)
            # 判断返回值不为空
            if self.txt_box1.get() != '':
                # 删除用户环境下的所有中望的配置
                self.user_file = getenv("APPDATA").replace("\\", "/") + '/ZWSOFT/ZW3D'
                file_in_user_file = listdir(self.user_file)
                for each in file_in_user_file:
                    rmtree(self.user_file + '\\' + each)


                # 不存在sqldrivers,复制,存在不复制
                file_sqldrivers = self.txt_box1.get() + '/sqldrivers'
                if not path.exists(file_sqldrivers):
                    copytree(self.host_path + '/QT/sqldrivers', self.txt_box1.get() + '/sqldrivers')

                # 选择的中望的路径apilibs
                self.sel_zw_file = self.txt_box1.get() + '/apilibs'
                # 判断选择的目录不存在apilibs,不存在就新建
                if not path.exists(self.sel_zw_file):
                    makedirs(self.sel_zw_file)
                # 将mdsv5installpath.cfg复制到中望选择路径
                copy(self.host_path + '/mdsv5installpath.cfg', self.sel_zw_file)
                # 将mdsv5installpath.cfg复制到D盘mdsv5的apilibs下
                copy(self.host_path + '/mdsv5installpath.cfg', self.host_path + '/apilibs')
                # 将api复制到中望安装路径下的apilibs
                copy(file_path, self.sel_zw_file)


                # 将qt文件复制到中望安装路径下
                for each in file_names:
                    copy(self.host_path + "/QT/" + each, self.txt_box1.get())
                ###########################################################################
                # 中望UI替换-----替换安装目录下的..\Settings\4-expert\     --这个是超级用户
                # 1，关掉中望，，，重要
                # 2，替换 Action\zh_cn\user.zcui文件 ,,这是命令文件
                # 3，替换Environment-13\Controls\mds.zcui，，这是装配UI
                # 4，替换Environment-10\Controls\mds.zcui，，这是零件UI
                ###########################################################################
                # 2，替换 Action\zh_cn\user.zcui文件 ,,这是命令文件
                order_filepath = self.txt_box1.get() + '/' + 'Settings/4-Expert/Action'
                # order_filepath_cn = self.txt_box1.get() + '/' + 'Settings/4-Expert/Action/zh_cn'
                # order_filepath_en = self.txt_box1.get() + '/' + 'Settings/4-Expert/Action/en_US'

                # if not path.exists(order_filepath_cn):
                #     makedirs(order_filepath_cn)
                # if not path.exists(order_filepath_en):
                #     makedirs(order_filepath_en)
                # copy(self.host_path + '/Default/User.zcui', order_filepath_cn)
                # copy(self.host_path + '/Default/System.zcui', order_filepath_cn)
                # copy(self.host_path + '/Default/System.zcui', order_filepath_en)
                # copy(self.host_path + '/Default/User.zcui', order_filepath_en)
                copy(self.host_path + '/Default/User.zcui',order_filepath)
                # 3，替换Environment-13\Controls\mds.zcui，，这是装配UI
                # 4，替换Environment-10\Controls\mds.zcui，，这是零件UI
                asm_ui_file = self.txt_box1.get() + '/' + 'Settings/4-Expert/Environment-13/Controls'
                prt_ui_file = self.txt_box1.get() + '/' + 'Settings/4-Expert/Environment-10/Controls'
                drw_ui_file = self.txt_box1.get() + '/' + 'Settings/4-Expert/Environment-4/Controls'
                open_ui_file = self.txt_box1.get() + '/' + 'Settings/4-Expert/Environment-0/Controls'
                copy(self.host_path + '/Default/mds.zcui',asm_ui_file)
                copy(self.host_path + '/Default/mds.zcui',prt_ui_file)
                copy(self.host_path + '/Default/mds.zcui',drw_ui_file)
                copy(self.host_path + '/Default/mds.zcui',open_ui_file)
                self.zw_log = '中望MDS插件配置完成'

                # 将图片放入中望的安装目录下
                # 中望icon位置
                zw_icon_path = self.txt_box1.get() + '/' + 'ZWMold/Resource/Icons'
                # 安装包的icon
                icon_listfile = listdir(self.host_path + '/icon')
                for each in icon_listfile:
                    copy(self.host_path + '/icon/' + each, zw_icon_path)
                # 将版本号写入数据库(完成版需要取消注释)
                # self.connect_sql()
                # 执行完提示文件复制完成
                #messagebox.showinfo('提示', '中望文件配置完成,请关闭窗口或配置其他文件')
                # self.application_window.quit()
            else:
                self.zw_log = '中望MDS插件未配置'
                return

        except Exception as e:
            # for each in popen('tasklist'):
            #     if each.lower().find('zw3d') >= 0:
            #         self.zw_in_process = '检测到中望未关闭,请关闭中望后重新尝试'
            #         self.zw_log = '中望MDS插件未配置'
            #         #messagebox.showerror('错误', e)
            #         messagebox.showerror('信息', self.zw_in_process)
            #         return
            # else:
            self.zw_log = '中望MDS插件未配置'
            messagebox.showerror('信息', e)
            return

    # 复制到CREO的路径下
    def copy_file_CREO(self):
        #  复制文件到creo的安装目录D:\PTC\Creo 4.0\M050\Common Files\x86e_win64\obj路径下
        # qt5core.dll
        # qt5gui.dll
        # qt5sql.dll
        # qt5svg.dll
        # qt5widgets.dll
        # 复制文件夹platforms和imageformats和plugins到上面的目录
        file_names = ["Qt5Gui.dll", "Qt5Core.dll", "Qt5Sql.dll", "Qt5Svg.dll", "Qt5Widgets.dll","libmysql.dll"]
        try:
            for each in popen('tasklist'):
                if each.lower().find('creo') >= 0:
                    self.creo_log = 'Creo文件未配置'
                    self.creo_in_process = '检测到Creo未关闭,请关闭Creo后重新尝试'
                    messagebox.showerror('错误', self.creo_in_process)
                    return
            # creo_path路径
            # creo_version 路径中的版本号
            creo_path = 'D:/PTC/Creo 4.0/' + self.creo_version + '/Common Files/x86e_win64/obj'
            if path.exists(creo_path):
                if not path.exists(creo_path + '/platforms'):
                    copytree(self.host_path + '/QT/platforms', creo_path + '/platforms')
                if not path.exists(creo_path + '/imageformats'):
                    copytree(self.host_path + '/QT/imageformats', creo_path + '/imageformats')
                if not path.exists(creo_path + '/plugins'):
                    copytree(self.host_path + '/QT/plugins', creo_path + '/plugins')
                for each in file_names:
                    copy(self.host_path + "/QT/" + each, creo_path)
            self.creo_log = 'Creo文件已配置完成'
        except Exception as e:
            self.creo_log = 'Creo文件未配置'
            messagebox.showerror('错误', e)
            return

    # 复制到Catia路径下
    def copy_file_Catia(self):
        try:
            # 将Catia文件复制到C盘（C:\ProgramData\DassaultSystemes\CATEnv）下
            Catia_file = self.host_path + '/Catia/CATIA_P3.V5-6R2019.B29.txt'
            Catia_copy_path = 'C:/ProgramData/DassaultSystemes/CATEnv'
            if path.exists(Catia_copy_path):
                copy(Catia_file, Catia_copy_path)
            else:
                makedirs(Catia_copy_path)
                copy(Catia_file, Catia_copy_path)
            #catia_log = 'Catia文件已配置完成,请关闭窗口或配置其他文件'
            #messagebox.showinfo('信息',catia_log)
        except Exception as e:
            messagebox.showerror('错误', e)

    # 执行确定按钮
    def copy_confirm(self):
        if self.var_zw.get() == 1:
            self.copy_file_ZW()
        else:
            self.zw_log='中望MDS插件未配置'
        if self.var_creo.get() == 1:
            self.copy_file_CREO()
        else:
            self.creo_log = 'Creo MDS插件未配置'
        # if self.var1_catia.get() == 1:
        #     self.copy_file_Catia()
        #     self.catia_log = 'Catia MDS配置完成'
        # else:
        #     self.catia_log = 'Catia MDS未配置'
        filename = './ZW_path.txt'
        with open(filename, 'w') as file_object:
            file_object.write(self.txt_box1.get())
        messagebox.showinfo('信息', self.zw_log + '\n' + self.creo_log + '\n')

    # 连接数据库，写入数据
    def connect_sql(self):
        host = '10.244.147.169'
        user = 'mds'
        pwd = 'MDA_mds!@#2019'
        port = 3306
        db = 'mds2'
        connection = pymysql.connect(host=host, user=user, password=pwd, port=port, db=db, charset='utf8')
        cur = connection.cursor()

        # 当前登陆用户的用户名work_id
        work_id = getpass.getuser()
        # group name
        # start time
        # end time
        # remark
        # user current version

        try:
            # 获取最大id
            sql_get_maxid = 'select max(id) from mdspermission_user'
            cur.execute(sql_get_maxid)
            max_id = cur.fetchone()[0]

            # 获得数据库中的workid
            sql_get_work_id = 'select workid from mdspermission_user'
            cur.execute(sql_get_work_id)
            workid = cur.fetchall()

            # 遍历数据库workid，如果存在当前用户的workid，就更新当前用户的当前版本
            flag = False
            for each in workid:
                if each[0] == work_id:
                    flag = True
                    sql_update = "update mdspermission_user set user_current_version = '%s' where workid = '%s'" % (
                    VERSION, work_id)
                    cur.execute(sql_update)
                    connection.commit()
                    break
            # 如果当前是新用户，将新用户的当前版本号插入表
            if not flag:
                # 插入数据
                sql_insert = "insert into mdspermission_user (id,workid,user_current_version) values (%i,'%s','%s')" % (
                    max_id + 1, work_id, VERSION)
                cur.execute(sql_insert)
                connection.commit()
        # 发生错误回退
        except Exception as e:
            connection.rollback()
        # 关闭游标和数据库
        finally:
            cur.close()
            connection.close()


if __name__ == '__main__':

    window = Window()
