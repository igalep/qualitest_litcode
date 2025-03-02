#selenium task 

run :

python -m venv ./venv/slenium_qualitest 
source ./venv/slenium_qualitest/bin/activate    
pip install -r requirements.txt   
pytest tests/test_amazon_select_item.py --browser=chrome   (or firefox or edge)