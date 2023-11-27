import datetime
import os
import time
import wget
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import StartBrowser


date = "".join(str(datetime.date.today()).split("-"))


browser = StartBrowser.Start_Lap("EntertainBuddy")
browser.implicitly_wait(15)

browser.get("https://colab.research.google.com/drive/1ISvpY3YSeBKvdYj99uSP3bPADZwABQvV?usp=sharing")
act = ActionChains(browser)
act.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
act.key_down(Keys.CONTROL)
act.send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
f = open(os.path.dirname(__file__) + "//Data//" + date + "_script.txt", "r")
content = f.readlines()
print(content)
stripped_content = ""
for i in content:
    stripped_content += i.strip()
    stripped_content = stripped_content.replace("\"", " ")
text = stripped_content
prompt = """
!pip install g2p_en
!pip install fairseq
from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
from fairseq.models.text_to_speech.hub_interface import TTSHubInterface
import IPython.display as ipd
from google.colab import files
import scipy
import numpy

models, cfg, task = load_model_ensemble_and_task_from_hf_hub("facebook/fastspeech2-en-ljspeech",arg_overrides={"vocoder": "hifigan", "fp16": False})
model = models[0]
TTSHubInterface.update_cfg_with_data_cfg(cfg, task.data_cfg)
generator = task.build_generator(models, cfg)

text = "%s"

sample = TTSHubInterface.get_model_input(task, text)
wav, rate = TTSHubInterface.get_prediction(task, model, generator, sample)
scipy.io.wavfile.write("%s.wav",rate = rate,data=wav.numpy())
files.download("%s.wav")
ipd.Audio(wav, rate=rate)
""" % (text.strip(),date.strip(),date.strip())
act.send_keys(prompt).perform()
act.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()

#browser.find_element(By.XPATH,'//mwc-button[text()="Run anyway"]').click()
time.sleep(20)
wait = WebDriverWait(browser,10000)
print("Audio Preparing")
while True:
    if os.path.exists(f"//Data//{date}.wav"):
        break
browser.quit()
