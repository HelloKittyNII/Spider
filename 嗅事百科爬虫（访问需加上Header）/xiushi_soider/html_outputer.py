#coding=utf-8

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return

        self.datas.append(data)


    def outpute_html(self):
        fout = open("outputer.html",'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")


        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s<td>" % data['url'])
            fout.write("<td>%s<td>" % data['content'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")
