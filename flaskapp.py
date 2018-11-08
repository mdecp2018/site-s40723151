#coding：utf-8
來自flask導入Flask，send_from_directory，請求，重定向，\
    render_template，session，make_response，url_for，flash
隨機導入
導入數學
進口口
#init.py為自行建立的起始物件
import init
＃利用nocache.py建立@nocache decorator，讓頁面不會留下緩存
來自nocache import nocache
＃以下是cmsimfly
進口重新
進口口
導入數學
import hashlib
#use quote_plus（）生成URL
import urllib.parse
#use cgi.escape（）類似於php htmlspecialchars（）
#use cgi.escape（）或html.escape為textarea標籤生成數據，否則Editor無法處理一些Javascript代碼。
導入cgi
導入系統
#for new parse_content函數
#from bs4 import BeautifulSoup
＃為了使用bs4.element，改為import bs4
導入bs4
#ssavePage和savePage
import shutil

＃獲取文件的當前目錄
_curdir = os.path.join（os.getcwd（），os.path.dirname（__ file__））
sys.path.append（_curdir）

#by init.py中的uwsgi = False或True決定在uwsgi模式或近端模式執行

#ends for cmsimfly

＃假如隨後要利用blueprint架構時，可以將程式放在子目錄中
＃然後利用register方式導入
＃導入g1目錄下的user1.py
#import users.g1.user1

＃確定程式檔案所在目錄，在Windows有最後的反斜線
_curdir = os.path.join（os.getcwd（），os.path.dirname（__ file__））
＃表示程式在近端執行，最後必須決定是由init.py或此地決定目錄設定
config_dir = _curdir +“/ config /”
static_dir = _curdir +“/ static”
download_dir = _curdir +“/ downloads /”
image_dir = _curdir +“/ images /”

＃利用init.py啟動，建立所需的相關檔案
initobj = init.Init（）
＃cancel init.py中初始類別中的類uwsgi變數（靜態變量）設定
uwsgi = init.Init.uwsgi

＃必須先將download_dir設為static_folder，然後才可以用於下載方法中的app.static_folder的呼叫
app = Flask（__ name__）

＃設置隨後要在藍圖應用程式中引用的全局變數
app.config ['config_dir'] = config_dir
app.config ['static_dir'] = static_dir
app.config ['download_dir'] = download_dir

#use用session必須要設置secret_key
＃為了使用會話，您必須設置密鑰
＃設置密鑰。保持這個秘密：
app.secret_key ='A0Zr9 @ 8j / 3yX R~XHH！jmN] LWX /，？R @ T'

＃子目錄中註冊藍圖位置
＃app.register_blueprint（users.g1.user1.g1app）


@ app.route（'/ checkLogin'，methods = ['POST']）
def checkLogin（）：
    msgstr“”“檢查用戶登錄過程。”“
    password = request.form [“password”]
    site_title，saved_pa​​ssword = parse_config（）
    hashed_pa​​ssword = hashlib.sha512（password.encode（'utf-8'））。hexdigest（）
    如果hashed_pa​​ssword == saved_pa​​ssword：
        session ['admin'] = 1
        return redirect（'/ edit_page'）
    返回重定向（'/'）

 
@ app.route（'/ delete_file'，methods = ['POST']）
def delete_file（）：
    msgstr“”“刪除用戶上傳的文件。”“
    如果不是isAdmin（）：
        return redirect（“/ login”）
    head，level，page = parse_content（）
    directory = render_menu（head，level，page）
    filename = request.form ['filename']
    如果filename是None：
        outstring =“沒有選擇文件！”
        return set_css（）+“<div class ='container'> <nav>”+ \
                   目錄+“</ nav> <section> <h1>刪除錯誤</ h1>”+ \
                   超越+“<br/> <br /> </ body> </ html>”
    outstring =“刪除所有這些文件？<br /> <br />”
    outstring + =“<form method ='post'action ='doDelete'>”
    ＃只選擇了一個文件
    if isinstance（filename，str）：
        outstring + = filename +“<input type ='hidden'name ='filename'value ='”+ \
                            文件名+“'> <br />”
    其他：
        ＃多個文件被選中
        對於範圍內的索引（len（文件名））：
            outstring + = filename [index] +“<input type ='hidden'name ='filename'value ='”+ \
                                filename [index] +“'> <br />”
    outstring + =“<br /> <input type ='submit'value ='delete'> </ form>”

    return set_css（）+“<div class ='container'> <nav>”+ \
               目錄+“</ nav> <section> <h1>下載列表</ h1>”+ \
               超越+“<br/> <br /> </ body> </ html>”


@ app.route（'/ doDelete'，methods = ['POST']）
def doDelete（）：
    msgstr“”“刪除用戶上傳文件的操作。”“
    如果不是isAdmin（）：
        return redirect（“/ login”）
    ＃ 刪除文件
    filename = request.form ['filename']
    outstring =“所有這些文件都將被刪除：<br /> <br />”
    ＃只選擇一個文件
    if isinstance（filename，str）：
        嘗試：
            os.remove（download_dir +“/”+ filename）
            outstring + = filename +“刪除！”
        除了：
            outstring + = filename +“錯誤，無法刪除文件！<br />”
    其他：
        ＃多個文件被選中
        對於範圍內的索引（len（文件名））：
            try:
                os.remove(download_dir + "/" + filename[index])
                outstring += filename[index] + " deleted!<br />"
            except:
                outstring += filename[index] + "Error, can not delete files!<br />"

    head, level, page = parse_content()
    directory = render_menu(head, level, page)

    return set_css() + "<div class='container'><nav>" + \
               directory + "</nav><section><h1>Download List</h1>" + \
               outstring + "<br/><br /></body></html>"


@ app.route（'/ doSearch'，methods = ['POST']）
def doSearch（）：
    msgstr“”“使用關鍵字搜索content.htm的行動”“”
    如果不是isAdmin（）：
        return redirect（“/ login”）
    其他：
        keyword = request.form ['keyword']
        head，level，page = parse_content（）
        directory = render_menu（head，level，page）
        match =“”
        對於範圍內的索引（len（head））：
            if（keyword！=“”或None）和（page.index]中的keyword.lower（）.lower（）或\
            head [index] .lower（））中的keyword.lower（）：\
                匹配+ =“<a href='/get_page/" + head[index] +”'>“+ \
                                頭[索引] +“</a> <br />”
        return set_css（）+“<div class ='container'> <nav>”+ \
                   目錄+“</ nav> <section> <h1>搜索結果</ h1>關鍵字：”+ \
                   keyword.lower（）+“<br /> <br />在以下幾頁：<br /> <br />”+ \
                   匹配+“</ section> </ div> </ body> </ html>”


@ app.route（'/ download /'，methods = ['GET']）
def下載（）：
    msgstr“”“使用URL下載文件。”“”
    filename = request.args.get（'filename'）
    type = request.args.get（'type'）
    如果type ==“files”：
        return send_from_directory（download_dir，filename = filename）
    其他：
    ＃用於圖像文件
        return send_from_directory（image_dir，filename = filename）
    

@ app.route（'/ download_list'，methods = ['GET']）
def download_list（）：
    msgstr“”“列出下載目錄中的文件。”“
    如果不是isAdmin（）：
        return redirect（“/ login”）
    其他：
        如果不是request.args.get（'edit'）：
            編輯= 1
        其他：
            edit = request.args.get（'edit'）
        如果不是request.args.get（'page'）：
            page = 1
        其他：
            page = request.args.get（'page'）
        如果不是request.args.get（'item_per_page'）：
            item_per_page = 10
        其他：
            item_per_page = request.args.get（'item_per_page'）
        如果不是request.args.get（'keyword'）：
            keyword =“”
        其他：
            keyword = request.args.get（'keyword'）
            session ['download_keyword'] =關鍵字
    files = os.listdir（download_dir）
    如果關鍵字不是“”：
        files = [elem in elem in files if if str（keyword）in elem]
    files.sort（）
    total_rows = len（文件）
    totalpage = math.ceil（total_rows / int（item_per_page））
    starti = int（item_per_page）*（int（page） -  1）+ 1
    endi = starti + int（item_per_page） -  1
    outstring =“<form method ='post'action ='delete_file'>”
    notlast =假
    如果total_rows> 0：
        超越+ =“<br />”
        if（int（page）* int（item_per_page））<total_rows：
            notlast = True
        if int（page）> 1：
            outstring + =“<a href ='”
            outstring + =“download_list？＆amp; page = 1＆amp; item_per_page =”+ str（item_per_page）+ \
                                “＆amp; keyword =”+ str（session.get（'download_keyword'））
            outtring + =“'> <<< / a>”
            page_num = int（page） -  1
            outstring + =“<a href ='”
            outstring += "download_list?&amp;page=" + str(page_num) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>Previous</a> "

        span = 10

        for index in range(int(page)-span, int(page)+span):
            if index>= 0 and index< totalpage:
                page_now = index + 1 
                if page_now == int(page):
                    outstring += "<font size='+1' color='red'>" + str(page) + " </font>"
                else:
                    outstring += "<a href='"
                    outstring += "download_list?&amp;page=" + str(page_now) + "&amp;item_per_page=" + \
                                        str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
                    outstring += "'>"+str(page_now) + "</a> "

        if notlast == True:
            nextpage = int(page) + 1
            outstring += " <a href='"
            outstring += "download_list?&amp;page=" + str(nextpage) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>Next</a>"
            outstring += " <a href='"
            outstring += "download_list?&amp;page=" + str(totalpage) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>>></a><br /><br />"

        if (int(page) * int(item_per_page)) < total_rows:
            notlast = True
            outstring += downloadlist_access_list(files, starti, endi) + "<br />"
        else:
            outstring += "<br /><br />"
            outstring += downloadlist_access_list(files, starti, total_rows) + "<br />"

        if int(page) > 1:
            outstring += "<a href='"
            outstring += "download_list?&amp;page=1&amp;item_per_page=" + str(item_per_page) + \
                                "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'><<</a> "
            page_num = int(page) - 1
            outstring += "<a href='"
            outstring += "download_list?&amp;page=" + str(page_num) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>Previous</a> "

        span = 10

        對於範圍內的索引（int（page）-span，int（page）+ span）：
        #for（$ j = $ page- $ range; $ j <$ page + $ range; $ j ++）
            如果index> = 0且index <totalpage：
                page_now = index + 1
                如果page_now == int（頁面）：
                    outstring + =“<font size ='+ 1'color ='red'>”+ str（page）+“</ font>”
                其他：
                    outstring + =“<a href ='”
                    outstring + =“download_list？＆amp; page =”+ str（page_now）+ \
                                        “＆amp; item_per_page =”+ str（item_per_page）+ \
                                        “＆amp; keyword =”+ str（session.get（'download_keyword'））
                    outstring + =“'>”+ str（page_now）+“</a>”

        if notlast == True：
            nextpage = int（page）+ 1
            outstring += " <a href='"
            outstring += "download_list?&amp;page=" + str(nextpage) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>Next</a>"
            outstring += " <a href='"
            outstring += "download_list?&amp;page=" + str(totalpage) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>>></a>"
    else:
        outstring += "no data!"
    outtring + =“<br /> <br /> <input type ='submit'value ='delete'> <input type ='reset'value ='reset'> </ form>”

    head，level，page = parse_content（）
    directory = render_menu（head，level，page）

    return set_css（）+“<div class ='container'> <nav>”+ \
               目錄+“</ nav> <section> <h1>下載列表</ h1>”+ outstring +“<br/> <br /> </ body> </ html>”


def downloadlist_access_list（files，starti，endi）：
    msgstr“”“list_list的列表文件功能。”“
    ＃提供了不同的擴展文件，相關鏈接
    #popup窗口可以查看圖像，視頻或STL文件，其他文件可以直接下載
    #file是要列出的所有數據，從starti到endi
    #add文件大小
    outstring =“”
    對於範圍內的索引（int（starti）-1，int（endi））：
        fileName，fileExtension = os.path.splitext（files [index]）
        fileExtension = fileExtension.lower()
        fileSize = sizeof_fmt(os.path.getsize(download_dir+"/"+files[index]))
        # images files
        if fileExtension == ".png" or fileExtension == ".jpg" or fileExtension == ".gif":
            outstring += '<input type="checkbox" name="filename" value="' + \
                              files[index] + '"><a href="javascript:;" onClick="window.open(\'/images/'+ \
                              files [index] +'\'，\'images \'，\'catalogmode \'，\'scrollbars \'）“>'+ \
                              files [index] +'</a>（'+ str（fileSize）+'）<br />'
        #stl文件
        elif fileExtension ==“。stl”：
            outstring + ='<input type =“checkbox”name =“filename”value =“'+ \
                              files [index] +'“> <a href =”javascript：;“onClick =”window.open（\'/ static / viewstl.html？src = / downloads /'+ \
                              files [index] +'\'，\'images \'，\'catalogmode \'，\'scrollbars \'）“>'+ \
                              files [index] +'</a>（'+ str（fileSize）+'）<br />'
        #flv文件
        elif fileExtension ==“。flv”：
            outstring + ='<input type =“checkbox”name =“filename”value =“'+ \
                              files [index] +'“> <a href =”javascript：;“onClick =”window.open（\'/ flvplayer？filepath = / downloads /'+ \
            files [index] +'\'，\'images \'，\'catalogmode \'，\'scrollbars \'）“>'+ files [index] +'</a>（'+ str（fileSize）+' ）<br />'
        ＃直接下載文件
        其他：
            outstring + =“<input type ='checkbox'name ='filename'value ='”+ files [index] + \
                              “'> <a href='/downloads/"+ files[index] +”'>“+ files [index] + \
                              “</a>（”+ str（fileSize）+“）<br />”
    回歸過度


#download方法主要將位於下載目錄下的檔案送回瀏覽器
@ app.route（'/下載/ <路徑：路徑>'）
def下載（路徑）：
    msgstr“”“在下載目錄中發送文件。”“
    return send_from_directory（_curdir +“/ downloads /”，path）


＃與file_selector搭配的取檔程式
def downloadselect_access_list（files，starti，endi）：
    msgstr“”“伴隨著file_selector。”“
    outstring =“”
    對於範圍內的索引（int（starti）-1，int（endi））：
        fileName，fileExtension = os.path.splitext（files [index]）
        fileSize = os.path.getsize（download_dir +“/”+ files [index]）
        outstring + ='''<input type =“checkbox”name =“filename”value =“'''+ \
                          files [index] +'''“> <a href =”＃“onclick ='window.setLink（”/ downloads /'''+ \
                          files [index] +'''“，0）; return false;'>'''+ files [index] + \
                          '''</a>（'''+ str（sizeof_fmt（fileSize））+'''）<br />'''
    回歸過度


@ app.route（'/ edit_config'，defaults = {'edit'：1}）
@ app.route（'/ edit_config / <路徑：編輯>'）
def edit_config（編輯）：
    msgstr“”“配置編輯html表單。”“
    head，level，page = parse_content（）
    directory = render_menu（head，level，page）
    如果不是isAdmin（）：
        return set_css（）+“<div class ='container'> <nav>”+ \
                 目錄+“</ nav> <section> <h1>登錄</ h1> <form method ='post'action ='checkLogin'> \
                 密碼：<輸入類型='密碼'名稱='密碼'> \
                 <input type ='submit'value ='login'> </ form> \
                 </節> </ DIV> </ BODY> </ HTML>“
    其他：
        site_title，password = parse_config（）
        #edit配置文件
        return set_css（）+“<div class ='container'> <nav>”+ \
                 目錄+“</ nav> <section> <h1>編輯配置</ h1> <form method ='post'action ='saveConfig'> \
                 網站標題：<input type ='text'name ='site_title'value ='“+ site_title +”'size = '50'> <br /> \
                 密碼：<input type ='text'name ='password'value ='“+ password +”'size = '50'> <br /> \
                 <input type ='hidden'name ='password2'value ='“+ password +”'> \
                 <input type ='submit'value ='send'> </ form> \
                 </節> </ DIV> </ BODY> </ HTML>“


＃編輯所有頁面內容
@ app.route（'/ edit_page'，defaults = {'edit'：1}）
@ app.route（'/ edit_page / <路徑：編輯>'）
def edit_page（編輯）：
    “”頁面編輯html表單。“”“
    ＃檢查管理員是否
    如果不是isAdmin（）：
        return redirect（'/ login'）
    其他：
        head，level，page = parse_content（）
        directory = render_menu（head，level，page）
        pagedata = file_get_contents（config_dir +“content.htm”）
        outstring = tinymce_editor（directory，cgi.escape（pagedata））
        回歸過度


def editorfoot（）：
    返回'''<body>'''


def editorhead（）：
    返回'''
    <br />
<！ -  <script src =“// cdn.tinymce.com/4/tinymce.min.js”> </ script>  - >
<script src =“/ static / tinymce4 / tinymce / tinymce.min.js”> </ script>
<script src =“/ static / tinymce4 / tinymce / plugins / sh4tinymce / plugin.min.js”> </ script>
<link rel =“stylesheet”href =“/ static/tinymce4/tinymce/plugins/sh4tinymce/style/style.css”>
<SCRIPT>
tinymce.init（{
  選擇器：“textarea”，
  身高：500，
  element_format：“html”，
  語言：“en”，
  valid_elements：'* [*]'，
  extended_valid_elements：“script [language | type | src]”，
  插件：[
    'advlist autolink list鏈接圖像charmap打印預覽hr anchor pagebreak'，
    'searchreplace wordcount visualblocks visualchars code fullscreen'，
    'insertdatetime media nonbreaking save table contextmenu directionality'，
    '表情符號模板粘貼textcolor colorpicker textpattern imagetools sh4tinymce'
  ]
  toolbar1：'insertfile save undo redo | styleselect | 粗體斜體| alignleft aligncenter alignright alignjustify | bullist numlist outdent indent'，
  toolbar2：'鏈接圖片| 打印預覽媒體| forecolor backcolor表情符號| 代碼sh4tinymce'，
  relative_urls：false，
  toolbar_items_size：'小'，
  file_picker_callback：function（callback，value，meta）{
        cmsFilePicker（callback，value，meta）;
    }，
  模板：[
    {title：'測試模板1'，內容：'測試1'}，
    {title：'測試模板2'，內容：'測試2'}
  ]
  content_css：[
    “//fonts.googleapis.com/css?family=Lato:300,300i,400,400i”，
    “//www.tinymce.com/css/codepen.min.css”
  ]
}）;

function cmsFilePicker（callback，value，meta）{
    tinymce.activeEditor.windowManager.open（{
        標題：'上傳的文件瀏覽器'，
        url：'/ file_selector？type ='+ meta.filetype，
        寬度：800，
        身高：550，
    }，{
        oninsert：function（url，objVals）{
            回調（url，objVals）;
        }
    }）;
};
</ SCRIPT>
'''


@ app.route（'/ error_log中'）
def error_log（self，info =“Error”）：
    head，level，page = parse_content（）
    directory = render_menu（head，level，page）
    return set_css() + "<div class='container'><nav>" + \
             directory + "</nav><section><h1>ERROR</h1>" + info + "</section></div></body></html>"


def file_get_contents(filename):
    # open file in utf-8 and return file content
    with open(filename, encoding="utf-8") as file:
        return file.read()


# 與 file_selector 配合, 用於 Tinymce4 編輯器的檔案選擇
def file_lister(directory, type=None, page=1, item_per_page=10):
    files = os.listdir(directory)
    total_rows = len(files)
    totalpage = math.ceil(total_rows/int(item_per_page))
    starti = int(item_per_page) * (int(page) - 1) + 1
    endi = starti + int(item_per_page) - 1
    outstring = file_selector_script()
    notlast = False
    if total_rows > 0:
        outstring += "<br />"
        if (int(page) * int(item_per_page)) < total_rows:
            notlast = True
        if int(page) > 1:
            outstring += "<a href='"
            outstring += "file_selector?type=" + type + \
                              "&amp;page=1&amp;item_per_page=" + \
                              str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'><<</a> "
            page_num = int(page) - 1
            outstring += "<a href='"
            outstring += "file_selector?type=" + type + \
                              "&amp;page=" + str(page_num) + \
                              "&amp;item_per_page=" +str(item_per_page) + \
                              “＆amp; keyword =”+ str（session.get（'download_keyword'））
            outstring + =“'>上一頁</a>”
        span = 10
        對於範圍內的索引（int（page）-span，int（page）+ span）：
            如果index> = 0且index <totalpage：
                page_now = index + 1 
                如果page_now == int（頁面）：
                    outstring + =“<font size ='+ 1'color ='red'>”+ str（page）+“</ font>”
                其他：
                    outstring + =“<a href ='”
                    outstring + =“file_selector？type =”+ type +“＆amp; page =”+ \
                                      str（page_now）+“＆amp; item_per_page =”+ \
                                      str（item_per_page）+“＆amp; keyword =”+ \
                                      STR（session.get（'download_keyword'））
                    outstring + =“'>”+ str（page_now）+“</a>”

        if notlast == True：
            nextpage = int（page）+ 1
            outstring + =“<a href ='”
            outstring + =“file_selector？type =”+ type +“＆amp; page =”+ \
                               str（nextpage）+“＆amp; item_per_page =”+ \
                               str（item_per_page）+“＆amp; keyword =”+ \
                               STR（session.get（'download_keyword'））
            outtring + =“'>下一步</a>”
            outstring + =“<a href ='”
            outstring + =“file_selector？type =”+ type +“＆amp; page =”+ \
                               str（totalpage）+“＆amp; item_per_page =”+ \
                               str（item_per_page）+“＆amp; keyword =”+ \
                               STR（session.get（'download_keyword'））
            outtring + =“'>>> </a> <br /> <br />”
        if（int（page）* int（item_per_page））<total_rows：
            notlast = True
            如果type ==“file”：
                outtring + = downloadselect_access_list（files，starti，endi）+“<br />”
            其他：
                outstring + = imageselect_access_list（files，starti，endi）+“<br />”
        其他：
            超越+ =“<br /> <br />”
            如果type ==“file”：
                outstring + = downloadselect_access_list（files，starti，total_rows）+“<br />”
            其他：
                outstring + = imageselect_access_list（files，starti，total_rows）+“<br />”
        if int（page）> 1：
            outstring + =“<a href ='”
            outstring + =“file_selector？type =”+ type + \
                              “＆amp; page = 1＆amp; item_per_page =”+ str（item_per_page）+ \
                              “＆amp; keyword =”+ str（session.get（'download_keyword'））
            outtring + =“'> <<< / a>”
            page_num = int（page） -  1
            outstring + =“<a href ='”
            outstring + =“file_selector？type =”+ type +“＆amp; page =”+ \
                               str（page_num）+“＆amp; item_per_page =”+ \
                               str（item_per_page）+“＆amp; keyword =”+ \
                               STR（session.get（'download_keyword'））
            outstring + =“'>上一頁</a>”
        span = 10
        對於範圍內的索引（int（page）-span，int（page）+ span）：
            如果index> = 0且index <totalpage：
                page_now = index + 1
                如果page_now == int（頁面）：
                    outstring + =“<font size ='+ 1'color ='red'>”+ str（page）+“</ font>”
                其他：
                    outstring + =“<a href ='”
                    outstring + =“file_selector？type =”+ type +“＆amp; page =”+ \
                                       str（page_now）+“＆amp; item_per_page =”+ \
                                       str（item_per_page）+“＆amp; keyword =”+ \
                                       STR（session.get（'download_keyword'））
                    outstring + =“'>”+ str（page_now）+“</a>”
        if notlast == True：
            nextpage = int（page）+ 1
            outstring + =“<a href ='”
            outstring + =“file_selector？type =”+ type +“＆amp; page =”+ \
                               str（nextpage）+“＆amp; item_per_page =”+ \
                               str（item_per_page）+“＆amp; keyword =”+ \
                               STR（session.get（'download_keyword'））
            outstring += "'>Next</a>"
            outstring += " <a href='"
            outstring += "file_selector?type=" + type + "&amp;page=" + \
                               str(totalpage) + "&amp;item_per_page=" + \
                               str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>>></a>"
    else:
        outstring += "no data!"

    if type == "file":
        return outstring+"<br /><br /><a href='fileuploadform'>file upload</a>"
    else:
        return outstring+"<br /><br /><a href='imageuploadform'>image upload</a>"


＃配合Tinymce4讓使用者透過html編輯器引用所上傳的文件與圖像
@ app.route（'/ file_selector'，methods = ['GET']）
def file_selector（）：
    如果不是isAdmin（）：
        return redirect（“/ login”）
    其他：
        如果不是request.args.get（'type'）：
            type =“file”
        其他：
            type = request.args.get（'type'）
        如果不是request.args.get（'page'）：
            page = 1
        其他：
            page = request.args.get（'page'）
        如果不是request.args.get（'item_per_page'）：
            item_per_page = 10
        其他：
            item_per_page = request.args.get（'item_per_page'）
        如果不是request.args.get（'keyword'）：
            keyword =無
        其他：
            keyword = request.args.get（'keyword'）

        如果type ==“file”：

            return file_lister（download_dir，type，page，item_per_page）
        elif type ==“image”：
            return file_lister（image_dir，type，page，item_per_page）


def file_selector_script（）：
    返回'''
<script language =“javascript”type =“text / javascript”>
$（函數（）{
    $（'。a'）。on（'click'，function（event）{
        setLink（）;
    }）;
}）;

function setLink（url，objVals）{
    top.tinymce.activeEditor.windowManager.getParams（）。oninsert（url，objVals）;
    top.tinymce.activeEditor.windowManager.close（）;
    返回虛假;
}
</ SCRIPT>
'''


@ app.route（'/ fileaxupload'，methods = ['POST']）
#ajax jquery用於燒瓶的chunked文件上傳
def fileaxupload（）：
    if isAdmin（）：
        ＃需要考慮上傳的文件名是否已經存在。
        ＃現在所有已存在的文件都將被新文件替換
        filename = request.args.get（“ax-file-name”）
        flag = request.args.get（“start”）
        if flag ==“0”：
            file = open（_curdir +“/ downloads /”+ filename，“wb”）
        其他：
            file = open（_curdir +“/ downloads /”+ filename，“ab”）
        file.write（request.stream.read（））
        file.close（）
        返回“上傳的文件！”
    其他：
        return redirect（“/ login”）


@ app.route（'/ fileuploadform'，defaults = {'edit'：1}）
@ app.route（'/ fileuploadform / <路徑：編輯>'）
def fileuploadform（編輯）：
    if isAdmin（）：
        head，level，page = parse_content（）
        directory = render_menu（head，level，page）
        return set_css（）+“<div class ='container'> <nav>”+ \
                 目錄+“</ nav> <section> <h1>文件上傳</ h1>”+ \
                 '''<script src =“/ static / jquery.js”type =“text / javascript”> </ script>
<script src =“/ static / axuploader.js”type =“text / javascript”> </ script>
<SCRIPT>
$（文件）。就緒（函數（）{
$（'。prova'）。axuploader（{url：'fileaxupload'，allowExt：['jpg'，'png'，'gif'，'7z'，'pdf'，'zip'，'flv'，'stl '，'瑞士法郎']，
表面處理：函數（X，文件）
    {
        alert（'所有文件已上傳：'+文件）;
    }，
啟用：真實，
remotePath：函數（）{
return'download /';
}
}）;
}）;
</ SCRIPT>
<div class =“prova”> </ div>
<input type =“button”onclick =“$（'。prova'）。axuploader（'disable'）”value =“asd”/>
<input type =“button”onclick =“$（'。prova'）。axuploader（'enable'）”value =“ok”/>
</節> </ BODY> </ HTML>
'''
    其他：
        return redirect（“/ login”）


@ app.route（'/ flvplayer'）
＃需要檢視能否取得文件路徑變數
def flvplayer（filepath = None）：
    outstring ='''
<object type =“application / x-shockwave-flash”data =“/ static / player_flv_multi.swf”width =“320”height =“240”>
     <param name =“movie”value =“player_flv_multi.swf”/>
     <param name =“allowFullScreen”value =“true”/>
     <param name =“FlashVars”value =“flv ='''+ filepath +'''＆amp; width = 320＆amp; height = 240＆amp; showstop = 1＆amp; showvolume = 1＆amp; showtime = 1
     ＆安培; startimage = /靜態/ startimage_en.jpg＆安培; showfullscreen = 1＆安培; bgcolor1 = 189ca8＆安培; bgcolor2 = 085c68
     ＆amp; playercolor = 085c68“/>
</對象>
'''
    回歸過度


@ app.route（'/ generate_pages'）
def generate_pages（）：
    ＃必須決定如何處理重複標題頁面的轉檔
    進口口
    ＃確定程式檔案所在目錄，在Windows有最後的反斜線
    _curdir = os.path.join（os.getcwd（），os.path.dirname（__ file__））
    ＃根據content.htm內容，逐一產生各頁面檔案
    ＃在此也要同時配合render_menu2，產生對應的錨鏈結
    head，level，page = parse_content（）
    ＃處理重複標題head數列，再重複標題按照次序加上1,2,3 ......
    newhead = []
    for i，v in enumerate（head）：
        ＃各重複標題總數
        totalcount = head.count（v）
        ＃目前重複標題出現總數
        count = head [：i] .count（v）
        ＃針對重複標題者，附加目前重複標題出現數+1，未重複採原標題
        newhead.append（v +“ - ”+ str（count + 1）if totalcount> 1 else v）
    ＃刪除內容目錄中所有html檔案
    filelist = [f表示os.listdir中的f（_curdir +“\\ content \\”）如果f.endswith（“。html”）]
    對於文件列表中的f：
        os.remove（os.path.join（_curdir +“\\ content \\”，f））
    ＃這裡需要建立專門寫出html的write_page
    #index.html
    file = open（_curdir +“\\ content \\ index.html”，“w”，encoding =“utf-8”）
    file.write（get_page2（None，newhead，0））
    file.close（）
    #sitemap
    file = open（_curdir +“\\ content \\ sitemap.html”，“w”，encoding =“utf-8”）
    #sitemap2需要newhead
    file.write（sitemap2（newhead））
    file.close（）
    ＃以下轉檔，改用newhead數列
    對於範圍內的我（len（newhead））：
        ＃在此必須要將頁面中的/ images /字組換換為images /，/ downloads /換為downloads /
        ＃因為Flask中靠/ images /取檔案，但是一般html則採相對目錄取檔案
        ＃此一字串置換在get_page2中進行
        file = open（_curdir +“\\ content \\”+ newhead [i] +“。html”，“w”，encoding =“utf-8”）
        ＃增加以newhead作為輸入
        file.write（get_page2（newhead [i]，newhead，0））
        file.close（）
    ＃在內容目錄下生成每個頁面的html
    返回“已經將網站轉為靜態網頁。<a href='/'>首頁</a>”
#seperate頁面需要標題和編輯變量，如果edit = 1，系統將進入編輯模式
＃單頁編輯將使用ssavePage保存內容，這意味著單獨保存頁面
@ app.route（'/ get_page'）
@ app.route（'/ get_page / <heading>'，defaults = {'edit'：0}）
@ app.route（'/ get_page / <標題> / <INT：編輯>'）
def get_page（標題，編輯）：
    head，level，page = parse_content（）
    directory = render_menu（head，level，page）
    如果標題為無：
        heading = head [0]
    ＃因為同一頭可能有多頁，因此不可使用head.index（heading）搜尋page_order
    page_order_list，page_content_list = search_content（head，page，heading）
    return_content =“”
    pagedata =“”
    outstring =“”
    outstring_duplicate =“”
    pagedata_duplicate =“”
    outstring_list = []
    對於範圍內的i（len（page_order_list））：
        #page_order = head.index（標題）
        page_order = page_order_list [i]
        如果page_order == 0：
            last_page =“”
        其他：
            last_page = head [page_order-1] +“<< <a href ='/ get_page /”+ \
                             head [page_order-1] +“'>上一頁</a>”
        如果page_order == len（head） -  1：
            #no next page
            next_page =“”
        其他：
            next_page =“<a href ='/ get_page /”+ head [page_order + 1] + \
                              “'>下一個</a> >>”+ head [page_order + 1]
        如果len（page_order_list）> 1：
            return_content + = last_page +“”+ next_page + \
                                      “<br /> <h1>”+標題+“</ h1>”+ \
                                      page_content_list [i] +“<br />”+ \
                                      last_page +“”+ next_page +“<br /> <hr>”
            pagedata_duplicate =“<h”+ level [page_order] +“>”+標題+ \
                                          “</ h”+級別[page_order] +“>”+ page_content_list [i]
            outstring_list.append（last_page +“”+ next_page +“<br />”+ tinymce_editor（directory，cgi.escape（pagedata_duplicate），page_order））
        其他：
            return_content + = last_page +“”+ next_page +“<br /> <h1>”+ \
                                      標題+“</ h1>”+ page_content_list [i] +“<br />”+ last_page +“”+ next_page
            
        pagedata + =“<h”+ level [page_order] +“>”+ heading +“</ h”+ level [page_order] +“>”+ page_content_list [i]
        ＃利用cgi.escape（）將specialchar轉成只能顯示的格式
        outstring + = last_page +“”+ next_page +“<br />”+ tinymce_editor（目錄，cgi.escape（pagedata），page_order）
    
    ＃edit = 0表示查看頁面
    如果編輯== 0：
        return set_css（）+“<div class ='container'> <nav>”+ \
                 目錄+“</ nav> <section>”+ return_content +“</ section> </ div> </ body> </ html>”
    ＃進入編輯模式
    其他：
        ＃檢查管理員是否
        如果不是isAdmin（）：
            重定向（url_for（'登錄'））
        其他：
            如果len（page_order_list）> 1：
                ＃若碰到重複頁面頁印，且要求編輯，則導向edit_page
                #return redirect（“/ edit_page”）
                對於範圍內的i（len（page_order_list））：
                    outstring_duplicate + = outstring_list [i] +“<br /> <hr>”
                return outstring_duplicate
            其他：
            #pataata =“<h”+ level [page_order] +“>”+ heading +“</ h”+ level [page_order] +“>”+ search_content（head，page，heading）
            #outstring = last_page +“”+ next_page +“<br />”+ tinymce_editor（目錄，cgi.escape（pagedata），page_order）
                回歸過度


#seperate頁面需要標題和編輯變量，如果edit = 1，系統將進入編輯模式
＃單頁編輯將使用ssavePage保存內容，這意味著單獨保存頁面
'''
@ app.route（'/ get_page2'）
@ app.route（'/ get_page2 / <heading>'，defaults = {'edit'：0}）
@ app.route（'/ get_page2 / <標題> / <INT：編輯>'）
'''
def get_page2（heading，head，edit）：
    not_used_head，level，page = parse_content（）
    ＃直接在此將/ images /換為./../ images /，/ downloads /換為./../downloads/,以內容為基準的相對目錄設定
    page = [w.replace（'/ images /'，'./../ images /'）for w in page]
    page = [w.replace（'/ downloads /'，'。/。/ download /'）for page in page]
    directory = render_menu2（head，level，page）
    如果標題為無：
        heading = head [0]
    ＃因為同一頭可能有多頁，因此不可使用head.index（heading）搜尋page_order
    page_order_list，page_content_list = search_content（head，page，heading）
    return_content =“”
    pagedata =“”
    outstring =“”
    outstring_duplicate =“”
    pagedata_duplicate =“”
    outstring_list = []
    對於範圍內的i（len（page_order_list））：
        #page_order = head.index（標題）
        page_order = page_order_list [i]
        如果page_order == 0：
            last_page =“”
        其他：
            #last_page = head [page_order-1] +“<< <a href ='/ get_page /”+ head [page_order-1] +“'>上一頁</a>”
            last_page = head [page_order-1] +“<< <a href ='”+ head [page_order-1] +“。html'>上一頁</a>”
        如果page_order == len（head） -  1：
            #no next page
            next_page =“”
        其他：
            #next_page =“<a href='/get_page/"+head[page_order+1] +”'>下一個</a> >>“+ head [page_order + 1]
            next_page =“<a href='"+ head[page_order+1] + ".html'>下一頁</a> >>”+ head [page_order + 1]
        如果len（page_order_list）> 1：
            return_content + = last_page +“”+ next_page +“<br /> <h1>”+ \
                                      標題+“</ h1>”+ page_content_list [i] + \
                                      “<br />”+ last_page +“”+ next_page +“<br /> <hr>”
            pagedata_duplicate = "<h"+level[page_order] + ">" + heading + "</h" + level[page_order]+">"+page_content_list[i]
            outstring_list.append(last_page + " " + next_page + "<br />" + tinymce_editor(directory, cgi.escape(pagedata_duplicate), page_order))
        else:
            return_content += last_page + " " + next_page + "<br /><h1>" + \
                                      heading + "</h1>" + page_content_list[i] + \
                                      "<br />" + last_page + " " + next_page
            
        pagedata += "<h" + level[page_order] + ">" + heading + \
                          "</h" + level[page_order] + ">" + page_content_list[i]
        # 利用 cgi.escape() 將 specialchar 轉成只能顯示的格式
        outstring += last_page + " " + next_page + "<br />" + tinymce_editor(directory, cgi.escape(pagedata), page_order)
    
    # edit=0 for viewpage
    if edit == 0:
        return set_css2() + "<div class='container'><nav>"+ \
        directory + "</nav><section>" + return_content + "</section></div></body></html>"
    # enter edit mode
    else:
        # check if administrator
        if not isAdmin():
            redirect(url_for('login'))
        else:
            if len(page_order_list) > 1:
                # 若碰到重複頁面頁印, 且要求編輯, 則導向 edit_page
                #return redirect（“/ edit_page”）
                對於範圍內的i（len（page_order_list））：
                    outstring_duplicate + = outstring_list [i] +“<br /> <hr>”
                return outstring_duplicate
            其他：
            #pataata =“<h”+ level [page_order] +“>”+ heading +“</ h”+ level [page_order] +“>”+ search_content（head，page，heading）
            #outstring = last_page +“”+ next_page +“<br />”+ tinymce_editor（目錄，cgi.escape（pagedata），page_order）
                回歸過度


@ app.route（'/ image_delete_file'，methods = ['POST']）
def image_delete_file（）：
    如果不是isAdmin（）：
        return redirect（“/ login”）
    filename = request.form ['filename']
    head，level，page = parse_content（）
    directory = render_menu（head，level，page）
    如果filename是None：
        outstring =“沒有選擇文件！”
        return set_css（）+“<div class ='container'> <nav>”+ \
                 目錄+“</ nav> <section> <h1>刪除錯誤</ h1>”+ \
                 超越+“<br/> <br /> </ body> </ html>”
    outstring =“刪除所有這些文件？<br /> <br />”
    outstring + =“<form method ='post'action ='image_doDelete'>”
    ＃只選擇了一個文件
    if isinstance（filename，str）：
        outstring + = filename +“<input type ='hidden'name ='filename'value ='”+ \
                          文件名+“'> <br />”
    其他：
        ＃多個文件被選中
        對於範圍內的索引（len（文件名））：
            outstring + = filename [index] +“<input type ='hidden'name ='filename'value ='”+ \
                              filename [index] +“'> <br />”
    outstring + =“<br /> <input type ='submit'value ='delete'> </ form>”

    return set_css（）+“<div class ='container'> <nav>”+ \
             目錄+“</ nav> <section> <h1>下載列表</ h1>”+ \
             超越+“<br/> <br /> </ body> </ html>”


@ app.route（'/ image_doDelete'，methods = ['POST']）
def image_doDelete（）：
    如果不是isAdmin（）：
        return redirect（“/ login”）
    ＃ 刪除文件
    filename = request.form ['filename']
    outstring =“所有這些文件都將被刪除：<br /> <br />”
    ＃只選擇一個文件
    if isinstance（filename，str）：
        嘗試：
            os.remove（image_dir +“/”+ filename）
            outstring + = filename +“刪除！”
        除了：
            outstring + = filename +“錯誤，無法刪除文件！<br />”
    其他：
        ＃多個文件被選中
        對於範圍內的索引（len（文件名））：
            嘗試：
                os.remove（image_dir +“/”+ filename [index]）
                outstring + = filename [index] +“刪除！<br />”
            除了：
                outstring += filename[index] + "Error, can not delete files!<br />"

    head, level, page = parse_content()
    directory = render_menu(head, level, page)

    return set_css() + "<div class='container'><nav>" + \
             directory + "</nav><section><h1>Image List</h1>" + \
             outstring + "<br/><br /></body></html>"


@app.route('/image_list', methods=['GET'])
def image_list():
    if not isAdmin():
        return redirect("/login")
    else:
        if not request.args.get('edit'):
            edit= 1
        else:
            edit = request.args.get('edit')
        if not request.args.get('page'):
            page = 1
        else:
            page = request.args.get（'page'）
        如果不是request.args.get（'item_per_page'）：
            item_per_page = 10
        其他：
            item_per_page = request.args.get（'item_per_page'）
        如果不是request.args.get（'keyword'）：
            keyword =“”
        其他：
            keyword = request.args.get（'keyword'）
            session ['image_keyword'] =關鍵字
    files = os.listdir（image_dir）
    如果關鍵字不是“”：
        files = [elem in elem in files if if str（keyword）in elem]
    files.sort（）
    total_rows = len（文件）
    totalpage = math.ceil（total_rows / int（item_per_page））
    starti = int（item_per_page）*（int（page） -  1）+ 1
    endi = starti + int（item_per_page） -  1
    outstring =“<form method ='post'action ='image_delete_file'>”
    notlast =假
    如果total_rows> 0：
        超越+ =“<br />”
        if（int（page）* int（item_per_page））<total_rows：
            notlast = True
        if int（page）> 1：
            outstring + =“<a href ='”
            outstring + =“image_list？＆amp; page = 1＆amp; item_per_page =”+ \
                              str（item_per_page）+“＆amp; keyword =”+ str（session.get（'image_keyword'））
            outtring + =“'> <<< / a>”
            page_num = int（page） -  1
            outstring + =“<a href ='”
            outstring + =“image_list？＆amp; page =”+ str（page_num）+ \
                              “＆amp; item_per_page =”+ str（item_per_page）+ \
                              “＆amp; keyword =”+ str（session.get（'image_keyword'））
            outstring + =“'>上一頁</a>”
        span = 10
        對於範圍內的索引（int（page）-span，int（page）+ span）：
            如果index> = 0且index <totalpage：
                page_now = index + 1 
                如果page_now == int（頁面）：
                    outstring + =“<font size ='+ 1'color ='red'>”+ str（page）+“</ font>”
                其他：
                    outstring + =“<a href ='”
                    outstring + =“image_list？＆amp; page =”+ str（page_now）+ \
                                      “＆amp; item_per_page =”+ str（item_per_page）+ \
                                      “＆amp; keyword =”+ str（session.get（'image_keyword'））
                    outstring + =“'>”+ str（page_now）+“</a>”

        if notlast == True：
            nextpage = int（page）+ 1
            outstring + =“<a href ='”
            outstring + =“image_list？＆amp; page =”+ str（nextpage）+ \
                              “＆amp; item_per_page =”+ str（item_per_page）+ \
                              “＆amp; keyword =”+ str（session.get（'image_keyword'））
            outtring + =“'>下一步</a>”
            outstring + =“<a href ='”
            outstring + =“image_list？＆amp; page =”+ str（totalpage）+ \
                              “＆amp; item_per_page =”+ str（item_per_page）+ \
                              “＆amp; keyword =”+ str（session.get（'image_keyword'））
            outtring + =“'>>> </a> <br /> <br />”
        if（int（page）* int（item_per_page））<total_rows：
            notlast = True
            outstring + = imagelist_access_list（files，starti，endi）+“<br />”
        其他：
            超越+ =“<br /> <br />”
            outstring + = imagelist_access_list（files，starti，total_rows）+“<br />”
        
        if int（page）> 1：
            outstring + =“<a href ='”
            outstring + =“image_list？＆amp; page = 1＆amp; item_per_page =”+ \
                              str（item_per_page）+“＆amp; keyword =”+ str（session.get（'image_keyword'））
            outtring + =“'> <<< / a>”
            page_num = int（page） -  1
            outstring + =“<a href ='”
            outstring + =“image_list？＆amp; page =”+ str（page_num）+ \
                              “＆amp; item_per_page =”+ str（item_per_page）+ \
                              “＆amp; keyword =”+ str（session.get（'image_keyword'））
            outstring + =“'>上一頁</a>”
        span = 10
        對於範圍內的索引（int（page）-span，int（page）+ span）：
            如果index> = 0且index <totalpage：
                page_now = index + 1
                如果page_now == int（頁面）：
                    outstring + =“<font size ='+ 1'color ='red'>”+ str（page）+“</ font>”
                其他：
                    outstring + =“<a href ='”
                    outstring + =“image_list？＆amp; page =”+ str（page_now）+ \
                                      “＆amp; item_per_page =”+ str（item_per_page）+ \
                                      “＆amp; keyword =”+ str（session.get（'image_keyword'））
                    outstring + =“'>”+ str（page_now）+“</a>”
        if notlast == True：
            nextpage = int（page）+ 1
            outstring + =“<a href ='”
            outstring + =“image_list？＆amp; page =”+ str（nextpage）+ \
                              “＆amp; item_per_page =”+ str（item_per_page）+ \
                              “＆amp; keyword =”+ str（session.get（'image_keyword'））
            outtring + =“'>下一步</a>”
            outstring + =“<a href ='”
            outstring + =“image_list？＆amp; page =”+ str（totalpage）+ \
                              “＆amp; item_per_page =”+ str（item_per_page）+ \
                              “＆amp; keyword =”+ str（session.get（'image_keyword'））
            outstring + =“'>>> </a>”
    其他：
        outstring + =“沒有數據！”
    outtring + =“<br /> <br /> <input type ='submit'value ='delete'> <input type ='reset'value ='reset'> </ form>”

    head，level，page = parse_content（）
    directory = render_menu（head，level，page）

    return set_css（）+“<div class ='container'> <nav>”+ \
             目錄+“</ nav> <section> <h1>圖像列表</ h1>”+ \
             超越+“<br/> <br /> </ body> </ html>”


@ app.route（'/ imageaxupload'，methods = ['POST']）
#ajax jquery用於燒瓶的chunked文件上傳
def imageaxupload（）：
    if isAdmin（）：
        ＃需要考慮上傳的文件名是否已經存在。
        ＃現在所有已存在的文件都將被新文件替換
        filename = request.args.get（“ax-file-name”）
        flag = request.args.get（“start”）
        if flag ==“0”：
            file = open（_curdir +“/ images /”+ filename，“wb”）
        其他：
            file = open（_curdir +“/ images /”+ filename，“ab”）
        file.write（request.stream.read（））
        file.close（）
        返回“上傳的圖片文件！”
    其他：
        return redirect（“/ login”）


def imagelist_access_list（files，starti，endi）：
    ＃提供了不同的擴展文件，相關鏈接
    #popup窗口可以查看圖像，視頻或STL文件，其他文件可以直接下載
    #file是要列出的所有數據，從starti到endi
    #add文件大小
    outstring = ""
    for index in range(int(starti)-1, int(endi)):
        fileName, fileExtension = os.path.splitext(files[index])
        fileExtension = fileExtension.lower()
        fileSize = sizeof_fmt(os.path.getsize(image_dir + "/" + files[index]))
        # images files
        if fileExtension == ".png" or fileExtension == ".jpg" or fileExtension == ".gif":
            outstring += '<input type="checkbox" name="filename" value="' + files[index] + \
                              '"><a href="javascript:;" onClick="window.open(\'/images/' + \
                              files[index] + '\',\'images\', \'catalogmode\',\'scrollbars\')">' + \
                              files [index] +'</a>（'+ str（fileSize）+'）<br />'
    回歸過度


＃與file_selector搭配的取影像檔程式
def imageselect_access_list（files，starti，endi）：
    outstring ='''<head>
<風格>
a.xhfbfile {padding：0 2px 0 0; line-height：1em;}
a.xhfbfile img {border：none; 保證金：6px;}
a.xhfbfile span {display：none;}
a.xhfbfile：懸停span {
    顯示：塊;
    位置：相對;
    左：150px;
    邊框：#aaa 1px solid;
    填充：2px;
    background-color：#ddd;
}
a.xhfbfile：懸停{
    background-color：#ccc;
    不透明度：.9;
    光標：指針;
}
</樣式>
</ HEAD>
'''
    對於範圍內的索引（int（starti）-1，int（endi））：
        fileName，fileExtension = os.path.splitext（files [index]）
        fileSize = os.path.getsize（image_dir +“/”+ files [index]）
        outstring + ='''<a class =“xhfbfile”href =“＃”onclick ='window.setLink（“/ images /'''+ \
                          files [index] +'''“，0）; return false;'>'''+ \
                          files [index] +'''<span style =“position：absolute; z-index：4;”> <br /> \
                          <img src =“/ images /'''+ files [index] +'''”width =“150px”/> </ span> </a> \
                          （'''+ str（sizeof_fmt（fileSize））+'''）<br />'''
    回歸過度


@ app.route（'/ imageuploadform'，defaults = {'edit'：1}）
@ app.route（'/ imageuploadform / <路徑：編輯>'）
def imageuploadform（編輯）：
    “”“圖片文件上傳表單”“”
    if isAdmin（）：
        head，level，page = parse_content（）
        directory = render_menu（head，level，page）
        return set_css（）+“<div class ='container'> <nav>”+ \
                 目錄+“</ nav> <section> <h1>圖像文件上傳</ h1>”+'''
<script src =“/ static / jquery.js”type =“text / javascript”> </ script>
<script src =“/ static / axuploader.js”type =“text / javascript”> </ script>
<SCRIPT>
$（文件）。就緒（函數（）{
$（'。prova'）。axuploader（{url：'imageaxupload'，allowExt：['jpg'，'png'，'gif']，
表面處理：函數（X，文件）
    {
        alert（'所有文件已上傳：'+文件）;
    }，
啟用：真實，
remotePath：函數（）{
返回'images /';
}
}）;
}）;
</ SCRIPT>
<div class =“prova”> </ div>
<input type =“button”onclick =“$（'。prova'）。axuploader（'disable'）”value =“asd”/>
<input type =“button”onclick =“$（'。prova'）。axuploader（'enable'）”value =“ok”/>
</節> </ BODY> </ HTML>
'''
    其他：
        return redirect（“/ login”）


@ app.route（'/'）
def index（）：
    head，level，page = parse_content（）
    ＃修復第一個中文標題錯誤
    return redirect（“/ get_page /”+ urllib.parse.quote_plus（head [0]））
    ＃以下將永遠不會執行
    directory = render_menu（head，level，page）
    如果標題為無：
        heading = head [0]
    ＃因為同一頭可能有多頁，因此不可使用head.index（heading）搜尋page_order
    page_order_list，page_content_list = search_content（head，page，heading）
    return_content =“”
    對於範圍內的i（len（page_order_list））：
        #page_order = head.index（標題）
        page_order = page_order_list [page_order_list [i]]
        如果page_order == 0：
            last_page =“”
        其他：
            last_page = head [page_order-1] +“<< <a href ='/ get_page /”+ \
                             head [page_order-1] +“'>上一頁</a>”
        如果page_order == len（head） -  1：
            #no next page
            next_page =“”
        其他：
            next_page =“<a href ='/ get_page /”+ head [page_order + 1] + \
                              “'>下一個</a> >>”+ head [page_order + 1]
        return_content + = last_page +“”+ next_page +“<br /> <h1>”+ \
                                  標題+“</ h1>”+ page_content_list [page_order_list [i]] + \
                                  “<br />”+ last_page +“”+ next_page

    return set_css（）+“<div class ='container'> <nav>”+ \
             目錄+“</ nav> <section>”+ return_content +“</ section> </ div> </ body> </ html>”


def isAdmin（）：
    如果session.get（'admin'）== 1：
            返回True
    其他：
        返回False


＃用於檢查目錄變量數據
@ app.route（'/ listdir同時'）
def listdir（）：
    return download_dir +“，”+ config_dir


@ app.route（'/ load_list'）
def load_list（item_per_page = 5，page = 1，filedir = None，keyword = None）：
    files = os.listdir（config_dir + filedir +“_ programs /”）
    如果關鍵字為無：
        通過
    其他：
        session ['search_keyword'] =關鍵字
        files = [如果是s中的關鍵字，則s為文件中的s]
    total_rows = len（文件）
    totalpage = math.ceil（total_rows / int（item_per_page））
    starti = int（item_per_page）*（int（page） -  1）+ 1
    endi = starti + int（item_per_page） -  1
    outstring ='''<script>
function keywordSearch（）{
    var oform = document.forms [“searchform”];
    //取元素集合中名屬性為keyword的值
    var getKeyword = oform.elements.keyword.value;
    //改為若表單為空，則列出全部資料
    // if（getKeyword！=“”）{
        window.location =“？brython＆keyword =”+ getKeyword;
    //}
}
</ SCRIPT>
    <form name =“searchform”>
    <input type =“text”id =“keyword”/>
    <input type =“button”id =“send”value =“查詢”onClick =“keywordSearch（）”/> 
    </ FORM>
'''
    outstring + =“<form name ='filelist'method ='post'action =''>”
    notlast =假
    如果total_rows> 0：
        ＃關閉頂部的頁面選擇器
        '''
        超越+ =“<br />”
        if（int（page）* int（item_per_page））<total_rows：
            notlast = True
        if int（page）> 1：
            outstring + =“<a href ='”
            outstring + =“brython？＆amp; page = 1＆amp; item_per_page =”+ str（item_per_page）+“＆amp; keyword =”+ str（session.get（'search_keyword'））
            outtring + =“'> {{</a>”
            page_num = int（page） -  1
            outstring + =“<a href ='”
            outstring + =“brython？＆amp; page =”+ str（page_num）+“＆amp; item_per_page =”+ str（item_per_page）+“＆amp; keyword =”+ str（session.get（'search_keyword'））
            outstring + =“'>上一頁</a>”
        span = 10
        對於範圍內的索引（int（page）-span，int（page）+ span）：
            如果index> = 0且index <totalpage：
                page_now = index + 1 
                如果page_now == int（頁面）：
                    outstring + =“<font size ='+ 1'color ='red'>”+ str（page）+“</ font>”
                其他：
                    outstring + =“<a href ='”
                    outstring + =“brython？＆amp; page =”+ str（page_now）+“＆amp; item_per_page =”+ str（item_per_page）+“＆amp; keyword =”+ str（session.get（'search_keyword'））
                    outstring + =“'>”+ str（page_now）+“</a>”

        if notlast == True：
            nextpage = int（page）+ 1
            outstring + =“<a href ='”
            outstring + =“brython？＆amp; page =”+ str（nextpage）+“＆amp; item_per_page =”+ str（item_per_page）+“＆amp; keyword =”+ str（session.get（'search_keyword'））
            outtring + =“'>下一步</a>”
            outstring + =“<a href ='”
            outstring + =“brython？＆amp; page =”+ str（totalpage）+“＆amp; item_per_page =”+ str（item_per_page）+“＆amp; keyword =”+ str（session.get（'search_keyword'））
            outtring + =“'>}} </a> <br /> <br />”
        '''
        if（int（page）* int（item_per_page））<total_rows：
            notlast = True
            outstring + = loadlist_access_list（files，starti，endi，filedir）+“<br />”
        其他：
            超越+ =“<br /> <br />”
            outstring + = loadlist_access_list（files，starti，total_rows，filedir）+“<br />”
        
        if int（page）> 1：
            outstring + =“<a href ='”
            outstring + =“/”+ filedir +“？＆amp; page = 1＆amp; item_per_page =”+ str（item_per_page）+“＆amp; keyword =”+ str（session.get（'search_keyword'））
            outtring + =“'> {{</a>”
            page_num = int（page） -  1
            outstring + =“<a href ='”
            outstring + =“/”+ filedir +“？＆amp; page =”+ str（page_num）+“＆amp; item_per_page =”+ \
                              str（item_per_page）+“＆amp; keyword =”+ str（session.get（'search_keyword'））
            outstring + =“'>上一頁</a>”
        span = 5
        對於範圍內的索引（int（page）-span，int（page）+ span）：
        #for（$ j = $ page- $ range; $ j <$ page + $ range; $ j ++）
            如果index> = 0且index <totalpage：
                page_now = index + 1
                如果page_now == int（頁面）：
                    outstring + =“<font size ='+ 1'color ='red'>”+ str（page）+“</ font>”
                其他：
                    outstring + =“<a href ='”
                    outstring + =“/”+ filedir +“？＆amp; page =”+ str（page_now）+ \
                                      “＆amp; item_per_page =”+ str（item_per_page）+ \
                                      “＆安培;關鍵字=”+ STR（session.get（'SEARCH_KEYWORD'））
                    outstring + =“'>”+ str（page_now）+“</a>”
        if notlast == True：
            nextpage = int（page）+ 1
            outstring + =“<a href ='”
            outstring + =“/”+ filedir +“？＆amp; page =”+ str（nextpage）+ \
                              “＆amp; item_per_page =”+ str（item_per_page）+ \
                              “＆amp; keyword =”+ str（session.get（'search_keyword'））
            outtring + =“'>下一步</a>”
            outstring + =“<a href ='”
            outstring + =“/”+ filedir +“？＆amp; page =”+ str（totalpage）+ \
                              “＆amp; item_per_page =”+ str（item_per_page）+ \
                              “＆amp; keyword =”+ str（session.get（'search_keyword'））
            outtring + =“'>}} </a>”
    其他：
        outstring + =“沒有數據！”
    #outstring + =“<br /> <br /> <input type ='submit'value ='load'> <input type ='reset'value ='reset'> </ form>”
    超越+ =“<br /> <br /> </ form>”

    回歸過度


def loadlist_access_list(files, starti, endi, filedir):
    # different extension files, associated links were provided
    # popup window to view images, video or STL files, other files can be downloaded directly
    # files are all the data to list, from starti to endi
    # add file size
    outstring = ""
    for index in range(int(starti)-1, int(endi)):
        fileName, fileExtension = os.path.splitext(files[index])
        fileExtension = fileExtension.lower()
        fileSize = sizeof_fmt(os.path.getsize(config_dir + filedir + "_programs/" + files[index]))
        # images files
        if fileExtension == ".png" or fileExtension == ".jpg" or fileExtension == ".gif":
            outstring + ='<input type =“checkbox”name =“filename”value =“'+ files [index] + \
                              '“> <a href =”javascript：;“onClick =”window.open（\'/ downloads /'+ \
                            files [index] +'\'，\'images \'，\'catalogmode \'，\'scrollbars \'）“>'+ files [index] +'</a>（'+ str（fileSize）+' ）<br />'
        #stl文件
        elif fileExtension ==“。stl”：
            outstring + ='<input type =“checkbox”name =“filename”value =“'+ files [index] +'”> <a href =“javascript：;” onClick =“window.open（\'/ static / viewstl.html？src = / downloads /'+ \
            files[index] + '\',\'images\', \'catalogmode\',\'scrollbars\')">' + files[index] + '</a> ('+str(fileSize)+')<br />'
        # flv files
        elif fileExtension == ".flv":
            outstring += '<input type="checkbox" name="filename" value="' + files[index] + '"><a href="javascript:;" onClick="window.open(\'/flvplayer?filepath=/downloads/' + \
            files[index]+'\',\'images\', \'catalogmode\',\'scrollbars\')">' + files[index] + '</a> ('+str(fileSize)+')<br />'
        # py files
        elif fileExtension == ".py":
            outstring + ='<input type =“radio”name =“filename”value =“'+ files [index] +'”>'+ files [index] +'（'+ str（fileSize）+'）<br / >“
        ＃直接下載文件
        其他：
            outstring + =“<input type ='checkbox'name ='filename'value ='”+ files [index] + \
                             “'> <a href='/"+ filedir +”_programs/" + files[index] +“'>”+ files [index] +“</a>（”+ str（fileSize）+“）<br />“
    回歸過度


@ app.route（'/登錄'）
def login（）：
    “”登錄例程“”“
    head，level，page = parse_content（）
    directory = render_menu（head，level，page）
    如果不是isAdmin（）：
        return set_css（）+“<div class ='container'> <nav>”+ \
                 目錄+“</ nav> <section> <h1>登錄</ h1> <form method ='post'action ='checkLogin'> \
                密碼：<輸入類型='密碼'名稱='密碼'> \
    <input type ='submit'value ='login'> </ form> \
    </節> </ DIV> </ BODY> </ HTML>“
    其他：
        return redirect（'/ edit_page'）


@ app.route（'/註銷'）
def logout（）：
    session.pop（'admin'，無）
    閃光燈（'已經登出！）
    return redirect（url_for（'login'））


def parse_config（）：
    如果不是os.path.isfile（config_dir +“config”）：
        ＃如果沒有配置文件，則創建配置文件
        file = open（config_dir +“config”，“w”，encoding =“utf-8”）
        #default password是admin
        密碼=“管理員”
        hashed_pa​​ssword = hashlib.sha512（password.encode（'utf-8'））。hexdigest（）
        file.write（“siteTitle：CMSimfly \ npassword：”+ hashed_pa​​ssword）
        file.close（）
    config = file_get_contents（config_dir +“config”）
    config_data = config.split（“\ n”）
    site_title = config_data [0] .split（“：”）[1]
    password = config_data [1] .split（“：”）[1]
    返回site_title，密碼


def _remove_h123_attrs（湯）：
    tag_order = 0
    對於soup.find_all中的標記（['h1'，'h2'，'h3']）：
        ＃假如標註內容沒有字串
        #if len（tag.text）== 0：
        如果len（tag.contents）== 0：
            ＃且該標註為排序第一
            如果tag_order == 0：
                tag.string =“第一個”
            其他：
                ＃若該標註非排序第一，則移除無內容的標題標註
                tag.extract（）
        ＃針對單一元件的標題標註
        elif len（tag.contents）== 1：
            ＃若內容非為純文字，表示內容為其他標註物件
            如果tag.get_text（）==“”：
                ＃且該標註為排序第一
                如果tag_order == 0：
                    # 在最前方插入標題
                    tag.insert_before(soup.new_tag('h1', 'First'))
                else:
                    # 移除 h1, h2 或 h3 標註, 只留下內容
                    tag.replaceWithChildren()
            # 表示單一元件的標題標註, 且標題為單一字串者
            else:
                # 判定若其排序第一, 則將 tag.name 為 h2 或 h3 者換為 h1
                if tag_order == 0:
                    tag.name = "h1"
            # 針對其餘單一字串內容的標註, 則保持原樣
        # 針對內容一個以上的標題標註
        #elif len(tag.contents) > 1:
        else:
            # 假如該標註內容長度大於 1
            # 且該標註為排序第一
            if tag_order == 0:
                # 先移除 h1, h2 或 h3 標註, 只留下內容
                #tag.replaceWithChildren()
                # 在最前方插入標題
                tag.insert_before(soup.new_tag('h1', 'First'))
            else:
                # 只保留標題內容,  去除 h1, h2 或 h3 標註
                ＃為了與前面的內文區隔，先在最前面插入br標註
                tag.insert_before（soup.new_tag（'BR'））
                ＃再移除非排序第一的h1，h2或h3標註，只留下內容
                tag.replaceWithChildren（）
        tag_order = tag_order + 1

    回湯

def parse_content（）：
    msgstr“”“使用bs4和re模塊函數來解析content.htm”“”
    #from pybean import Store，SQLiteWriter
    #if no content.db，使用cms表創建數據庫文件
    '''
    如果不是os.path.isfile（config_dir +“content.db”）：
        library = Store（SQLiteWriter（config_dir +“content.db”，frozen = False））
        cms = library.new（“cms”）
        cms.follow = 0
        cms.title =“頭1”
        cms.content =“內容1”
        cms.memo =“第一份備忘錄”
        library.save（CMS）
        library.commit（）
    '''
    ＃如果沒有content.htm，則生成head 1和content 1文件
    如果不是os.path.isfile（config_dir +“content.htm”）：
        如果沒有content.htm，則＃create content.htm
        File = open（config_dir +“content.htm”，“w”，encoding =“utf-8”）
        File.write（“<h1> head 1 </ h1> content 1”）
        File.close（）
    subject = file_get_contents（config_dir +“content.htm”）
    ＃處理沒有內容的內容
    如果主題==“”：
        如果沒有content.htm，則＃create content.htm
        File = open（config_dir +“content.htm”，“w”，encoding =“utf-8”）
        File.write（“<h1> head 1 </ h1> content 1”）
        File.clos e（）
        subject =“<h1> head 1 </ h1> content 1”
    ＃初始化返回列表
    head_list = []
    level_list = []
    page_list = []
    ＃從html內容中製作湯
    湯= bs4.BeautifulSoup（主題，'html.parser'）
    ＃嘗試解讀各種情況下的標題
    湯= _remove_h123_attrs（湯）
    ＃改寫content.htm後重新取主題
    使用open（config_dir +“content.htm”，“wb”）作為f：
        f.write（soup.encode（“UTF-8”））
    subject = file_get_contents（config_dir +“content.htm”）
    ＃將所有h1，h2，h3標籤放入列表中
    htag = soup.find_all（['h1'，'h2'，'h3']）
    n = len（htag）
    ＃獲取頁面內容以使用每個h標記分割主題
    temp_data = subject.split（str（htag [0]））
    如果len（temp_data）> 2：
        subject = str（htag [0]）。join（temp_data [1：]）
    其他：
        subject = temp_data [1]
    如果n> 1：
            #i從1到i-1
            對於範圍內的i（1，len（htag））：
                head_list.append（htag [I-1] .text.strip（））
                # use name attribute of h* tag to get h1, h2 or h3
                # the number of h1, h2 or h3 is the level of page menu
                level_list.append(htag[i-1].name[1])
                temp_data = subject.split(str(htag[i]))
                if len(temp_data) > 2:
                    subject = str(htag[i]).join(temp_data[1:])
                else:
                    subject = temp_data[1]
                # cut the other page content out of htag from 1 to i-1
                cut = temp_data[0]
                # add the page content
                page_list.append(cut)
    # last i
    # add the last page title
    head_list.append(htag[n-1].text.strip())
    # add the last level
    level_list.append(htag[n-1].name[1])
    temp_data = subject.split(str(htag[n-1]))
    # the last subject
    subject = temp_data[0]
    # cut the last page content out
    cut = temp_data[0]
    # the last page content
    page_list.append(cut)
    return head_list, level_list, page_list

def render_menu(head, level, page, sitemap=0):
    '''允許使用者在 h1 標題後直接加上 h3 標題, 或者隨後納入 h4 之後作為標題標註'''
    directory = ""
    # 從 level 數列第一個元素作為開端
    current_level = level[0]
    # 若是 sitemap 則僅列出樹狀架構而沒有套用 css3menu 架構
    if sitemap:
        directory += "<ul>"
    else:
        directory += "<ul id='css3menu1' class='topmenu'>"
    # 逐一配合 level 數列中的各標題階次, 一一建立對應的表單或 sitemap
    for index in range(len(head)):
        # 用 this_level 取出迴圈中逐一處理的頁面對應層級, 注意取出值為 str
        this_level = level[index]
        # 若處理中的層級比上一層級高超過一層, 則將處理層級升級 (處理 h1 後直接接 h3 情況)
        if (int(this_level) - int(current_level)) > 1:
            #this_level = str(int(this_level) - 1)
            # 考慮若納入 h4 也作為標題標註, 相鄰層級可能大於一層, 因此直接用上一層級 + 1
            this_level = str(int(current_level) + 1)
        # 若處理的階次比目前已經處理的階次大, 表示位階較低
        # 其實當 level[0] 完全不會報告此一區塊
        # 從正在處理的標題階次與前一個元素比對, 若階次低, 則要加入另一區段的 unordered list 標頭
        # 兩者皆為 str 會轉為整數後比較
        if this_level > current_level:
            directory += "<ul>"
            directory += "<li><a href='/get_page/" + head[index] + "'>" + head[index] + "</a>"
        # 假如正在處理的標題與前一個元素同位階, 則必須再判定是否為另一個 h1 的樹狀頭
        elif this_level == current_level:
            # 若正在處理的標題確實為樹狀頭, 則標上樹狀頭開始標註
            if this_level == 1:
                # 這裡還是需要判定是在建立 sitemap 模式或者選單模式
                if sitemap:
                    目錄+ =“<li> <a href='/get_page/" + head[index] +”'>“+ head [index] +”</a>“
                其他：
                    目錄+ =“<li class ='topmenu'> <a href='/get_page/" + head[index] +”'>“+ head [index] +”</a>“
            ＃假如不是樹狀頭，則只列出對應的清單
            其他：
                目錄+ =“<li> <a href='/get_page/" + head[index] +”'>“+ head [index] +”</a>“
        ＃假如正處理的元素比上一個元素位階更高，必須要先關掉前面的低位階區段
        其他：
            directory + =“</ li>”*（int（current_level） -  int（level [index]））
            directory + =“</ ul>”*（int（current_level） -  int（level [index]））
            如果this_level == 1：
                如果站點地圖：
                    目錄+ =“<li> <a href='/get_page/" + head[index] +”'>“+ head [index] +”</a>“
                其他：
                    目錄+ =“<li class ='topmenu'> <a href='/get_page/" + head[index] +”'>“+ head [index] +”</a>“
            其他：
                目錄+ =“<li> <a href='/get_page/" + head[index] +”'>“+ head [index] +”</a>“
        current_level = this_level
    目錄+ =“</ li> </ ul>”
    返回目錄
def render_menu2（head，level，page，sitemap = 0）：
    msgstr“”“靜態網站的渲染菜單”“”
    directory =“”
    current_level = level [0]
    如果站點地圖：
        目錄+ =“<ul>”
    其他：
        directory += "<ul id='css3menu1' class='topmenu'>"
    for index in range(len(head)):
        this_level = level[index]
        # 若處理中的層級比上一層級高超過一層, 則將處理層級升級 (處理 h1 後直接接 h3 情況)
        if (int(this_level) - int(current_level)) > 1:
            #this_level = str(int(this_level) - 1)
            this_level = str(int(current_level) + 1)
        if this_level > current_level:
            directory += "<ul>"
            #directory += "<li><a href='/get_page/"+head[index]+"'>"+head[index]+"</a>"
            # 改為連結到 content/標題.html
            directory += "<li><a href='" + head[index] + ".html'>" + head[index] + "</a>"
        elif this_level == current_level:
            如果this_level == 1：
                如果站點地圖：
                    ＃改為連結到content /標題.html
                    #directory + =“<li> <a href='/get_page/"+head[index]+"'>”+ head [index] +“</a>”
                    目錄+ =“<li> <a href='"+ head[index] + ".html'>”+ head [index] +“</a>”
                其他：
                    #directory + =“<li class ='topmenu'> <a href='/get_page/"+head[index]+"'>”+ head [index] +“</a>”
                    目錄+ =“<li class ='topmenu'> <a href='content/" + head[index] + ".html'>”+ head [index] +“</a>”
            其他：
                #directory + =“<li> <a href='/get_page/"+head[index]+"'>”+ head [index] +“</a>”
                目錄+ =“<li> <a href='"+ head[index] + ".html'>”+ head [index] +“</a>”
        其他：
            directory + =“</ li>”*（int（current_level） -  int（level [index]））
            directory + =“</ ul>”*（int（current_level） -  int（level [index]））
            如果this_level == 1：
                如果站點地圖：
                    #directory + =“<li> <a href='/get_page/"+head[index]+"'>”+ head [index] +“</a>”
                    目錄+ =“<li> <a href='"+ head[index] + ".html'>”+ head [index] +“</a>”
                其他：
                    #directory += "<li class='topmenu'><a href='/get_page/"+head[index]+"'>"+head[index]+"</a>"
                    directory += "<li class='topmenu'><a href='" + head[index] + ".html'>" + head[index] + "</a>"
            else:
                #directory += "<li><a href='/get_page/"+head[index]+"'>"+head[index]+"</a>"
                directory += "<li><a href='" + head[index] + ".html'>" + head[index] + "</a>"
        current_level = this_level
    directory += "</li></ul>"
    return directory
@app.route('/saveConfig', methods=['POST'])
def saveConfig():
    if not isAdmin():
        return redirect（“/ login”）
    site_title = request.form ['site_title']
    password = request.form ['password']
    password2 = request.form ['password2']
    如果site_title為None或密碼為None：
        return error_log（“沒有要保存的內容！”）
    old_site_title，old_password = parse_config（）
    head，level，page = parse_content（）
    directory = render_menu（head，level，page）
    如果site_title為None或密碼為None或password2！= old_password或password ==''：
        return set_css（）+“<div class ='container'> <nav>”+ \
                目錄+“</ nav> <section> <h1>錯誤！</ h1> <a href='/'>主頁</a> </ body> </ html>”
    其他：
        如果密碼==密碼2和密碼== old_password：
            hashed_pa​​ssword = old_password
        其他：
            hashed_pa​​ssword = hashlib.sha512（password.encode（'utf-8'））。hexdigest（）
        file = open(config_dir + "config", "w", encoding="utf-8")
        file.write("siteTitle:" + site_title + "\npassword:" + hashed_password)
        file.close()
        return set_css() + "<div class='container'><nav>" + \
                 directory + "</nav><section><h1>config file saved</h1><a href='/'>Home</a></body></html>"


@app.route('/savePage', methods=['POST'])
def savePage():
    """save all pages function"""
    page_content = request.form['page_content']
    # check if administrator
    if not isAdmin():
        return redirect("/login")
    if page_content is None:
        return error_log("no content to save!")
    # 在插入新頁面資料前, 先複製 content.htm 一分到 content_backup.htm
    shutil.copy2(config_dir + "content.htm", config_dir + "content_backup.htm")
    file = open(config_dir + "content.htm", "w", encoding="utf-8")
    # in Windows client operator, to avoid textarea add extra \n
    page_content = page_content.replace("\n","")
    file.write(page_content)
    file.close()

    # if every savePage generate_pages needed
    #generate_pages()
    '''
    # need to parse_content() to eliminate duplicate heading
    head, level, page = parse_content()
    file = open(config_dir + "content.htm", "w", encoding="utf-8")
    for index in range(len(head)):
        file.write("<h" + str(level[index])+ ">" + str(head[index]) + "</h" + str(level[index]) + ">" + str(page[index]))
    file.close()
    '''
    return redirect("/edit_page")


# use head title to search page content
'''
# search_content(head, page, search)
# 從 head 與 page 數列中, 以 search 關鍵字進行查詢
# 原先傳回與 search 關鍵字頁面對應的頁面內容
# 現在則傳回多重的頁面次序與頁面內容數列
find = lambda searchList, elem: [[i for i, x in enumerate(searchList) if x == e] for e in elem]
head = ["標題一","標題二","標題三","標題一","標題四","標題五"]
search_result = find(head,["標題一"])[0]
page_order = []
page_content = []
for i in range(len(search_result)):
    # 印出次序
    page_order.append(search_result[i])
    # 標題為 head[search_result[i]]
    #  頁面內容則為 page[search_result[i]]
    page_content.append(page[search_result[i]])
    # 從 page[次序] 印出頁面內容
# 準備傳回 page_order 與 page_content 等兩個數列
'''


def search_content(head, page, search):
    """search content"""
    ''' 舊內容
    return page[head.index(search)]
    '''
    find = lambda searchList, elem: [[i for i, x in enumerate(searchList) if x == e] for e in elem]
    search_result = find(head, [search])[0]
    page_order = []
    page_content = []
    for i in range(len(search_result)):
        # 印出次序
        page_order.append(search_result[i])
        # 標題為 head[search_result[i]]
        #  頁面內容則為 page[search_result[i]]
        page_content.append(page[search_result[i]])
        # 從 page[次序] 印出頁面內容
    # 準備傳回 page_order 與 page_content 等兩個數列
    return page_order, page_content


@app.route('/search_form', defaults={'edit': 1})
@app.route('/search_form/<path:edit>')
def search_form(edit):
    """form of keyword search"""
    if isAdmin():
        head, level, page = parse_content()
        directory = render_menu(head, level, page)
        return set_css() + "<div class='container'><nav>" + \
                 directory + "</nav><section><h1>Search</h1> \
                 <form method='post' action='doSearch'> \
                 keywords:<input type='text' name='keyword'> \
                 <input type='submit' value='search'></form> \
                 </section></div></body></html>"
    else:
        return redirect("/login")


# setup static directory
@app.route('/static/<path:path>')
def send_file(path):
    """send file function"""
    return app.send_static_file(static_dir + path)


# setup static directory
#@app.route('/images/<path:path>')
@app.route('/images/<path:path>')
def send_images(path):
    """send image files"""
    return send_from_directory(_curdir + "/images/", path)


# setup static directory
@app.route('/static/')
def send_static():
    """send static files"""
    return app.send_static_file('index.html')


# set_admin_css for administrator
def set_admin_css():
    """set css for admin"""
    outstring = '''<!doctype html>
<html><head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>計算機程式教材</title> \
<link rel="stylesheet" type="text/css" href="/static/cmsimply.css">
''' + syntaxhighlight()

    outstring += '''
<script src="/static/jquery.js"></script>
<script type="text/javascript">
$(function(){
    $("ul.topmenu> li:has(ul) > a").append('<div class="arrow-right"></div>');
    $("ul.topmenu > li ul li:has(ul) > a").append('<div class="arrow-right"></div>');
});
</script>
'''
    # SSL for uwsgi operation
    if uwsgi:
        outstring += '''
<script type="text/javascript">
if ((location.href.search(/http:/) != -1) && (location.href.search(/login/) != -1)) \
window.location= 'https://' + location.host + location.pathname + location.search;
</script>
'''
    site_title, password = parse_config()
    outstring += '''
</head><header><h1>''' + site_title + '''</h1> \
<confmenu>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/sitemap">SiteMap</a></li>
<li><a href="/edit_page">Edit All</a></li>
<li><a href="''' + str(request.url) + '''/1">Edit</a></li>
<li><a href="/edit_config">Config</a></li>
<li><a href="/search_form">Search</a></li>
<li><a href="/imageuploadform">Image Upload</a></li>
<li><a href="/image_list">Image List</a></li>
<li><a href="/fileuploadform">File Upload</a></li>
<li><a href="/download_list">File List</a></li>
<li><a href="/logout">Logout</a></li>
<li><a href="/generate_pages">generate_pages</a></li>
'''
    outstring += '''
</ul>
</confmenu></header>
'''
    return outstring


def set_css():
    """set css for dynamic site"""
    outstring = '''<!doctype html>
<html><head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>計算機程式教材</title> \
<link rel="stylesheet" type="text/css" href="/static/cmsimply.css">
''' + syntaxhighlight()

    outstring += '''
<script src="/static/jquery.js"></script>
<script type="text/javascript">
$(function(){
    $("ul.topmenu> li:has(ul) > a").append('<div class="arrow-right"></div>');
    $("ul.topmenu > li ul li:has(ul) > a").append('<div class="arrow-right"></div>');
});
</script>
'''
    if uwsgi:
        outstring += '''
<script type="text/javascript">
if ((location.href.search(/http:/) != -1) && (location.href.search(/login/) != -1)) \
window.location= 'https://' + location.host + location.pathname + location.search;
</script>
'''
    site_title, password = parse_config()
    outstring += '''
</head><header><h1>''' + site_title + '''</h1> \
<confmenu>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/sitemap">Site Map</a></li>
'''
    if isAdmin():
        outstring += '''
<li><a href="/edit_page">Edit All</a></li>
<li><a href="''' + str(request.url) + '''/1">Edit</a></li>
<li><a href="/edit_config">Config</a></li>
<li><a href="/search_form">Search</a></li>
<li><a href="/imageuploadform">image upload</a></li>
<li><a href="/image_list">image list</a></li>
<li><a href="/fileuploadform">file upload</a></li>
<li><a href="/download_list">file list</a></li>
<li><a href="/logout">logout</a></li>
<li><a href="/generate_pages">generate_pages</a></li>
'''
    else:
        outstring += '''
<li><a href="/login">login</a></li>
'''
    outstring += '''
</ul>
</confmenu></header>
'''
    return outstring


def set_css2():
    """set css for static site"""
    outstring = '''<!doctype html>
<html><head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>計算機程式教材</title> \
<link rel="stylesheet" type="text/css" href="./../static/cmsimply.css">
''' + syntaxhighlight2()

    outstring += '''
<script src="./../static/jquery.js"></script>
<script type="text/javascript">
$(function(){
    $("ul.topmenu> li:has(ul) > a").append('<div class="arrow-right"></div>');
    $("ul.topmenu > li ul li:has(ul) > a").append('<div class="arrow-right"></div>');
});
</script>
'''
    if uwsgi:
        outstring += '''
<script type="text/javascript">
if ((location.href.search(/http:/) != -1) && (location.href.search(/login/) != -1)) \
window.location= 'https://' + location.host + location.pathname + location.search;
</script>
'''
    site_title, password = parse_config()
    outstring += '''
</head><header><h1>''' + site_title + '''</h1> \
<confmenu>
<ul>
<li><a href="index.html">Home</a></li>
<li><a href="sitemap.html">Site Map</a></li>
<li><a href="./../reveal/index.html">reveal</a></li>
<li><a href="./../blog/index.html">blog</a></li>
'''
    outstring += '''
</ul>
</confmenu></header>
'''
    return outstring


def set_footer():
    """footer for page"""
    return "<footer> \
        <a href='/edit_page'>Edit All</a>| \
        <a href='" + str(request.url) + "/1'>Edit</a>| \
        <a href='edit_config'>Config</a> \
        <a href='login'>login</a>| \
        <a href='logout'>logout</a> \
        <br />Powered by <a href='http://cmsimple.cycu.org'>CMSimply</a> \
        </footer> \
        </body></html>"
@app.route('/sitemap', defaults={'edit': 1})
@app.route('/sitemap/<path:edit>')
def sitemap(edit):
    """sitemap for dynamic site"""
    head, level, page = parse_content()
    directory = render_menu(head, level, page)
    sitemap = render_menu(head, level, page, sitemap=1)
    return set_css() + "<div class='container'><nav>" + directory + \
             "</nav><section><h1>Site Map</h1>" + sitemap + \
             "</section></div></body></html>"
def sitemap2(head):
    """sitemap for static content generation"""
    edit = 0
    not_used_head, level, page = parse_content()
    directory = render_menu2(head, level, page)
    sitemap = render_menu2(head, level, page, sitemap=1)
    return set_css2() + "<div class='container'><nav>" + directory + \
             "</nav><section><h1>Site Map</h1>" + sitemap + \
             "</section></div></body></html>"


def sizeof_fmt(num):
    """size formate"""
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')
@app.route('/ssavePage', methods=['POST'])
def ssavePage():
    """seperate save page function"""
    page_content = request.form['page_content']
    page_order = request.form['page_order']
    if not isAdmin():
        return redirect("/login")
    if page_content is None:
        return error_log("no content to save!")
    # 請注意, 若啟用 fullpage plugin 這裡的 page_content tinymce4 會自動加上 html 頭尾標註
    page_content = page_content.replace("\n","")
    head, level, page = parse_content()
    original_head_title = head[int(page_order)]
    # 在插入新頁面資料前, 先複製 content.htm 一分到 content_backup.htm
    shutil.copy2(config_dir + "content.htm", config_dir + "content_backup.htm")
    file = open(config_dir + "content.htm", "w", encoding="utf-8")
    for index in range(len(head)):
        if index == int(page_order):
            file.write(page_content)
        else:
            file.write("<h"+str(level[index])+ ">" + str(head[index]) + "</h" + \
                          str(level[index])+">"+str(page[index]))
    file.close()
    # if every ssavePage generate_pages needed
    #generate_pages()

    # if head[int(page_order)] still existed and equal original_head_title, go back to origin edit status, otherwise go to "/"
    # here the content is modified, we need to parse the new page_content again
    head, level, page = parse_content()
    # for debug
    # print(original_head_title, head[int(page_order)])
    # 嘗試避免因最後一個標題刪除儲存後產生 internal error 問題
    if original_head_title is None:
        return redirect("/")
    if original_head_title == head[int(page_order)]:
        #edit_url = "/get_page/" + urllib.parse.quote_plus(head[int(page_order)]) + "&edit=1"
        #edit_url = "/get_page/" + urllib.parse.quote_plus(original_head_title) + "/1"
        edit_url = "/get_page/" + original_head_title + "/1"
        return redirect(edit_url)
    else:
        return redirect("/")


def syntaxhighlight():
    return '''
<script type="text/javascript" src="/static/syntaxhighlighter/shCore.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushJScript.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushJava.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushPython.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushSql.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushXml.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushPhp.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushLua.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushCpp.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushCss.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushCSharp.js"></script>
<link type="text/css" rel="stylesheet" href="/static/syntaxhighlighter/css/shCoreDefault.css"/>
<script type="text/javascript">SyntaxHighlighter.all();</script>

<!-- for LaTeX equations 暫時不用
    <script src="https://scrum-3.github.io/web/math/MathJax.js?config=TeX-MML-AM_CHTML" type="text/javascript"></script>
    <script type="text/javascript">
    init_mathjax = function() {
        if (window.MathJax) {
            // MathJax loaded
            MathJax.Hub.Config({
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\\\(","\\\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\\\[","\\\\]"] ]
                },
                displayAlign: 'left', // Change this to 'center' to center equations.
                "HTML-CSS": {
                    styles: {'.MathJax_Display': {"margin": 0}}
                }
            });
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
 -->
 <!-- 暫時不用
<script src="/static/fengari-web.js"></script>
<script type="text/javascript" src="/static/Cango-13v08-min.js"></script>
<script type="text/javascript" src="/static/CangoAxes-4v01-min.js"></script>
<script type="text/javascript" src="/static/gearUtils-05.js"></script>
-->
<!-- for Brython 暫時不用
<script src="https://scrum-3.github.io/web/brython/brython.js"></script>
<script src="https://scrum-3.github.io/web/brython/brython_stdlib.js"></script>
-->
<style>
img {
    border:4px solid blue;
}
</style>
'''



def syntaxhighlight2():
    return '''
<script type="text/javascript" src="./../static/syntaxhighlighter/shCore.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushJScript.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushJava.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushPython.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushSql.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushXml.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushPhp.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushLua.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushCpp.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushCss.js"></script>
<script type="text/javascript" src="./../static/syntaxhighlighter/shBrushCSharp.js"></script>
<link type="text/css" rel="stylesheet" href="./../static/syntaxhighlighter/css/shCoreDefault.css"/>
<script type="text/javascript">SyntaxHighlighter.all();</script>

<!-- for LaTeX equations 暫時不用
<script src="https://scrum-3.github.io/web/math/MathJax.js?config=TeX-MML-AM_CHTML" type="text/javascript"></script>
<script type="text/javascript">
init_mathjax = function() {
    if (window.MathJax) {
        // MathJax loaded
        MathJax.Hub.Config({
            tex2jax: {
                inlineMath: [ ['$','$'], ["\\\\(","\\\\)"] ],
                displayMath: [ ['$$','$$'], ["\\\\[","\\\\]"] ]
            },
            displayAlign: 'left', // Change this to 'center' to center equations.
            "HTML-CSS": {
                styles: {'.MathJax_Display': {"margin": 0}}
            }
        });
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    }
}
init_mathjax();
</script>
-->
<!-- 暫時不用
<script src="./../static/fengari-web.js"></script>
<script type="text/javascript" src="./../static/Cango-13v08-min.js"></script>
<script type="text/javascript" src="./../static/CangoAxes-4v01-min.js"></script>
<script type="text/javascript" src="./../static/gearUtils-05.js"></script>
-->
<!-- for Brython 暫時不用
<script src="https://scrum-3.github.io/web/brython/brython.js"></script>
<script src="https://scrum-3.github.io/web/brython/brython_stdlib.js"></script>
-->
<style>
img {
    border:4px solid blue;
}
</style>
'''


def tinymce_editor(menu_input=None, editor_content=None, page_order=None):
    sitecontent =file_get_contents(config_dir + "content.htm")
    editor = set_admin_css() + editorhead() + '''</head>''' + editorfoot()
    # edit all pages
    if page_order is None:
        outstring = editor + "<div class='container'><nav>" + \
                        menu_input + "</nav><section><form method='post' action='savePage'> \
                        <textarea class='simply-editor' name='page_content' cols='50' rows='15'>" +  \
                        editor_content + "</textarea><input type='submit' value='save'> \
                        </form></section></body></html>"
    else:
        # add viewpage button wilie single page editing
        head, level, page = parse_content()
        outstring = editor + "<div class='container'><nav>" + \
                        menu_input+"</nav><section><form method='post' action='/ssavePage'> \
                        <textarea class='simply-editor' name='page_content' cols='50' rows='15'>" + \
                        editor_content + "</textarea><input type='hidden' name='page_order' value='" + \
                        str(page_order) + "'><input type='submit' value='save'>"
        outstring += '''<input type=button onClick="location.href='/get_page/''' + \
                    head[page_order] + \
                    ''''" value='viewpage'></form></section></body></html>'''
    return outstring


def unique(items):
    """make items element unique"""
    found = set([])
    keep = []
    count = {}
    for item in items:
        if item not in found:
            count[item] = 0
            found.add(item)
            keep.append(item)
        else:
            count[item] += 1
            keep.append(str(item) + "_" + str(count[item]))
    return keep


if __name__ == "__main__":
    app.run()