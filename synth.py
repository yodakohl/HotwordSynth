import os
import os.path
from random import randint


voices=["english","english-north", "en-scottish", "english_rp", "english_wmids", "english-us", "mb-us1", "mb-us2", "mb-us3","mb-en1"]
words={"alexaA" : "\"[[a'lEksa]]\"", "alexaB":"\"[[@'lEksa]]\"", "alexaC":"\"[[@'lEksa]]\"?", "alexaD":"\"[[a'lEksa]]\"?"}

pitches= [10,40,60,80] #10 to 80
speeds=[80,100,120,170] #80 to 450
variants=["+m1","+m2","+m3","+m4","+m5","+m6","+m7","+f1","+f2","+f3","+f4"]
for word in words:
	for variant in variants:
		for voice in voices:
		#	for p in pitches:
		#	for s in speeds:
			p = randint(10, 80)
			s = randint(80,150)
		
			outfile = "./synth/Espeak_{}_{}_{}_{}_{}.wav".format(word,voice,p,s,variant)
			cmd = "echo {} | espeak -v {}{} -s {} -w {} ".format(words[word],voice,variant,s,outfile)
			os.system(cmd)


flite_voices=["kal", "kal16", "awb", "rms", "slt"]
flite_words={"alexaA" : "Alexa", "alexaB":"Alexa?", "alexaC":"Alexa!"}

for word in flite_words:
	for voice in flite_voices:
		outfile = "./synth/Flite_{}_{}.wav".format(word,voice)
		cmd = "flite -t {} -voice {} -o {}".format(flite_words[word],voice,outfile)
		os.system(cmd)


pico_lang= ["en-GB","en-US"]
for lang in pico_lang:
	for word in flite_words:
		outfile = "./synth/Pico_{}_{}.wav".format(word,lang)
		cmd = "pico2wave -l {} -w {} {}".format(lang,outfile,flite_words[word])
		os.system(cmd)


festival_voices=["voice_nitech_us_slt_arctic_hts",
	"voice_nitech_us_awb_arctic_hts", 
	"voice_nitech_us_bdl_arctic_hts", 
	"voice_nitech_us_clb_arctic_hts",
	"voice_nitech_us_jmk_arctic_hts", 
	"voice_nitech_us_rms_arctic_hts", 
	"voice_kal_diphone",
	"voice_ked_diphone", 
	"voice_cstr_us_awb_arctic_multisyn",
	"voice_cstr_us_jmk_arctic_multisyn",
	"voice_cmu_us_slt_arctic_hts",
	"voice_en1_mbrola",
	"voice_us1_mbrola"]

#for word in words:
#	for voice in festival_voices:
#		festival -b '({})' '(SayText "{}")'.format(voice,word)


#Ensure all Audio in mono 16Khz 16 bit int
#files = os.listdir("./synth")
#for f in files:
#	infile  = "./synth/"+f 
#	outfile = "./done/"+f 
#	cmd = "sox {} -c 1 -b 16 -r 16000 {}".format(infile,outfile)
#	os.system(cmd)











