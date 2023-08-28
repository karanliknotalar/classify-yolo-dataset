import requirements

requirements.check_req()

SAVE_IMAGE_SIZE = (500, 500)
IMG_FILES_DIR = r"C:\Users\ASUS\Desktop\semboller.v9i.yolov8\valid\images"
LABEL_FILES_DIR = r"C:\Users\ASUS\Desktop\semboller.v9i.yolov8\valid\labels"
CLASS_LIST = ['0', '1', '2', '2_adam_ustunde_oklu', '2_kare', '2_kare_ve_yuvarlak', '2_kat_kagit', '3',
              '3_adam_topluluk', '3gen_cetvel', '3gen_goz', '3gen_icinde_3gen', '3gen_ikili', '3gen_katmanli',
              '3gen_sekil', '3gen_ucak_3_noktali', '3top_cizgili', '3top_ince', '3top_kalin', '4', '4lu_ay_deseni',
              '6gen_ici_cizgili', '6gen_icinde_6gen', '6gen_ikili', '6gen_uclu', '7_numarali_askili_kiyafet',
              '7_okey_tasi', '8_gibi_desenli_sekil', '8top', 'abakus_sayi_sayma', 'abc', 'adam_eller_yukari',
              'adam_kafasi_yildirim_isaretli', 'adam_karateci', 'adam_vesikalik', 'afro_kafa', 'ag_tor_yuvarlakli',
              'agac_buyuk', 'agac_degisik', 'agac_desenli_tombul_minik_bocek', 'agac_kollu', 'agac_kucuk',
              'agac_yaninda_martili', 'agacli_yol', 'ahize_arti_isaretli', 'ahtapot_komik', 'ahtapot_oyuncak_kurdeleli',
              'ahtapot_saskin', 'ahtapot_sinirli', 'alarm_saat', 'alet_fise_takili', 'alet_ikili',
              'alet_ikili_kucuk_tombul', 'alet_ucu_yanlarinda_arti_isaretli', 'alev', 'ambulans_araba_arti_isaretli',
              'amerikan_topu_2_cizgili', 'anahtar', 'anahtar_disli_ayar_isareti', 'anahtar_disli_sapkali',
              'anahtar_hazine', 'anahtar_ilkel', 'anahtarlik', 'ara_beni_el_isareti', 'araba_2teker', 'araba_arazi',
              'araba_buyuk', 'araba_kapisiz', 'araba_kucuk', 'ari', 'artan_azalan_siralama',
              'arti_isareti_ortasi_yuvarlak', 'asagi_yukari_asansor_tusu', 'askida_havlu_askilik', 'askilik_dolgulu',
              'askilik_kucuk', 'astronot_tombul', 'at_duz', 'at_kafasi', 'at_kafasi_gozu_yok', 'at_satranc',
              'atari_oyun_kolu', 'ates', 'atki', 'atom', 'ay_cizgili', 'ay_yildiz', 'ay_yildiz_top_sekli',
              'ayak_insan_ayagi', 'ayakizi', 'ayakkabi_2tekerlekli', 'ayakkabi_3tekerlekli', 'ayakkabi_bagcikli',
              'ayakkabi_bayan', 'ayakkabi_bayan_toplu', 'ayakkabi_bot', 'ayakkabi_bot2', 'ayakkabi_bot3',
              'ayakkabi_gunluk', 'ayakkabi_klasik', 'ayakkabi_paten', 'ayakkabi_paten2', 'ayakkabi_paten3',
              'ayakkabi_spor', 'ayi_kafasi', 'ayi_korkunc', 'ayicik', 'ayicik_hayati_kaymis', 'ayna', 'ayna2',
              'b_seklinde_metre', 'baharat_el_degirmeni', 'baharatlik_seker_kabi', 'baklava_elmas_dikey_kesik_cizgili',
              'baklava_oklavasi_2li_capraz', 'balik_buyuk', 'balik_gibi_sus', 'balik_iki_cizgili', 'balik_kucuk',
              'balik_robot_kollu', 'balik_sise_gecirilmis', 'balon', 'balon_kutlama', 'balta', 'balta_egri_sapli',
              'balta_eski', 'bardak']
