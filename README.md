# ml
# mac install pipenv, need to disable csutial
mac: restart with command + R, run csrutil disable
# install ipykernel and start jupyter notebook with this ipykernel installed
pipenv install ipykernel
pipenv shell
python -m ipykernel install --user --name=my-virtualenv-name
jupyter notebook
# check python interpreter in jupyter notebook
import sys
print(sys.executable)
# pipenv install，在build dependencies的时候，不能使用python interpreter来执行一些阻塞进行的命令，比如matplotlib.pyplot
当执行pipenv install的时候，如果这个时候实行matplotlib.pylot进行绘图，会阻止pipenv install继续执行，同时，也会阻止pyplot进行绘图，会报kernel is dead类似的信息
