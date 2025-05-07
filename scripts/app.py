import pkg_resources
import pip 
package_name = "streamlit"
installed_packages = [pkg.key for pkg in pkg_resources.working_set]
if package_name in installed_packages:
    print(f"{package_name} is installed.")
else:
    print(f"{package_name} is not installed.")
    pip.main(['install', package_name])


import streamlit  as st 
import pickle 
import sklearn 
from numpy import exp

try : 
    lr = pickle.load(open('../artifacts/lr.pkl', 'rb'))
except Exception as e : 
    print(e)



x1 = st.number_input('dfd')
x2 = st.number_input('ddd')
x3 = st.number_input('dsdf')
x4 = st.number_input('sdfw')
x5 = st.number_input('3')
x6 = st.number_input('44')
x7 = st.number_input('df5d')
x8 = st.number_input('df6d')
x9 = st.number_input('dfss6d')
x10 = st.number_input('df6ssssd')
pred = lr.predict([[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]])

st.text(exp(pred))
