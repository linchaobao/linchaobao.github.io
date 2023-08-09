from bs4 import BeautifulSoup


publist = []

# parse index to get publist
with open("index.html", "r", encoding='UTF-8') as f:
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')


    publisttb = soup.find(id="baopublist") 
    for pubtr in publisttb.find_all('tr'):
        for pubtd in pubtr.find_all('td'):
            if pubtd.text.find('Linchao') == -1:
                continue
            print(pubtd)
            pubtdstr = str(pubtd)
            pubtdstr = pubtdstr.replace(r'<td>', '')
            pubtdstr = pubtdstr.replace(r'</td>', '')
            pubtdstr = pubtdstr.replace('\n', '')
            pubstrlist = pubtdstr.strip().split('<br/>')
            title = pubstrlist[0].strip()
            author = pubstrlist[1].strip()
            venue = pubstrlist[2].strip()
            pub = {'title': title,
                   'author': author,
                   'venue': venue}
            publist.append(pub)


print(publist)

# generate latex text 

# 
# \begin{itemize}
#     \item High-Fidelity 3D Digital Human Head Creation from RGB-D Selfies  (\href{https://github.com/tencent-ailab/hifi3dface}{project page})\\
#           \textbf{Linchao Bao}, Xiangkai Lin, Yajing Chen, Haoxian Zhang, Sheng Wang, Xuefei Zhe, Di Kang, Haozhi Huang, Xinwei Jiang, Jue Wang, Dong Yu, Zhengyou Zhang\\
#           \emph{ACM Transactions on Graphics (\textbf{TOG}), 2022} (\textbf{CCF-A, first author})
#     \item REALY: Rethinking the Evaluation of 3D Face Reconstruction  (\href{https://www.realy3dface.com/}{project page})\\
#           Zenghao Chai, Haoxian Zhang, Jing Ren, Di Kang, Zhengzhuo Xu, Xuefei Zhe, Chun Yuan*, \textbf{Linchao Bao*} (*corresponding author)\\
#           \emph{European Conference on Computer Vision (\textbf{ECCV}), 2022} (\textbf{CCF-B, corresponding author})
# \end{itemize}

latexstr = r'\begin{itemize}'

for pub in publist:
    latexstr += '\n    '
    latexstr += r'\item '
    latexstr += pub['title']
    latexstr += r'\\'
    latexstr += '\n        '
    latexstr += pub['author']
    latexstr += r'\\'
    latexstr += '\n        '
    latexstr += pub['venue']

latexstr += '\n'
latexstr += r'\end{itemize}'

# latexstr = latexstr.replace('Linchao Bao', r'\textbf{Linchao Bao}') 
latexstr = latexstr.replace(r'&', r'\&')
latexstr = latexstr.replace(r'<i>', r'\emph{')
latexstr = latexstr.replace(r'</i>', r'}')
latexstr = latexstr.replace(r'<b>', r'\textbf{')
latexstr = latexstr.replace(r'</b>', r'}')

with open("baopublist.txt", "w", encoding='UTF-8') as f:
    f.write(latexstr)