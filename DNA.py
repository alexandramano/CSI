#Eva
gender_f = "TGAAGGACCTTC"
race_w = "AAAACCTCA"
face_oval = "AGGCCTCA"
hair_blond = "TTAGCTATCGC"
eye_blue = "TTGTGGTGGC"

#Larisa
eye_brown = "AAGTAGTGAC"
hair_brown = "GCCAGTGCCG"

#Matej
gender_m = "TGCAGGAACTTC"
hair_black = "CCAGCAATCGC"

#Miha
hair_black = "CCAGCAATCGC"
eye_green = "GGGAGGTGGC"

DNA = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

if gender_f and race_w and hair_blond and eye_blue and face_oval in DNA:
    print "Eva is guilty!"
else:
    print "Eva is not guilty. Keep looking!"

if gender_f and race_w and face_oval and eye_brown and hair_brown in DNA:
    print "Larisa is guilty!"
else:
    print "Larisa is not guilty. Keep looking!"

if gender_m and race_w and face_oval and hair_black and eye_blue in DNA:
    print "Matej is guilty!"
else:
    print "Matej is not guilty. Keep looking!"

if gender_m and race_w and face_oval and hair_black and eye_green in DNA:
    print "Miha is guilty!"
else:
    print "Miha is not guilty! Keep looking!"