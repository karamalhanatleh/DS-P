# Write a function that takes as input an English sentence
#  (a string) and prints the total numberof vowels and the 
#  total number of consonants in thes entence.The function 
#  returns nothing. Note that the sentence could have special 
#  characters such as dots, dashes, and so on.



print("your welocme to code prints the "
      "  total number of Vowels and the "
      "  total number of consonants ")


def count_vow_con():

    sentence = input("enter the sentence : ")
  
    # تحويل الجمله الى small later لتسهيل عد الاحرف             
#ولحذف الفراغات                                              
    sentence_lower = sentence.lower().strip()

    vowels = ['a', 'i', 'o', 'u', 'e']
    count_vowels = 0
    count_consonants = 0
    for char in sentence_lower:
        if char in vowels:
            count_vowels += 1
        else:
            count_consonants += 1
    print("count vowels is :", count_vowels,
          "\nand count consonants is :", count_consonants)
    
    
    
count_vow_con()