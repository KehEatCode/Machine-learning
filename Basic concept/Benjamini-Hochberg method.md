# Benjamini- Hochberg method

- It's adjusts p-value in a way that limits the number of false positive that are reported as 'significat'
- adjusts p values means that it makes them larger
- 使得pvalue变大，不再显著（抛弃表面好但实质差的数值）

- step1: 根据原假设pvalue排序

- step2: 当p<= α *rank / m reject Ho

- 这里的α 是FDR threhold，一般为0.05

- Overlap

<img width="868" alt="Screen Shot 2022-08-11 at 3 11 27 PM" src="https://user-images.githubusercontent.com/93849914/184220438-667b4a42-62b4-4d8b-8ffa-61bc1d7af9b9.png">

<img width="994" alt="Screen Shot 2022-08-11 at 3 13 47 PM" src="https://user-images.githubusercontent.com/93849914/184220820-ea50d0c6-ebc5-4a9c-9599-87e667365931.png">
<img width="836" alt="Screen Shot 2022-08-11 at 3 15 25 PM" src="https://user-images.githubusercontent.com/93849914/184221096-481be398-4475-47ff-97d8-ccb5c6d42641.png">

## Result
<img width="1146" alt="Screen Shot 2022-08-11 at 3 16 02 PM" src="https://user-images.githubusercontent.com/93849914/184221189-7ccfa48e-8d99-450c-904b-d5f1242626e5.png">
<img width="963" alt="Screen Shot 2022-08-11 at 3 16 40 PM" src="https://user-images.githubusercontent.com/93849914/184221298-f5c77e50-9a38-425d-9c94-bc641f295ff9.png">
<img width="1148" alt="Screen Shot 2022-08-11 at 3 17 30 PM" src="https://user-images.githubusercontent.com/93849914/184221405-b0134de2-5fd7-4e22-896b-b6cfab4206db.png">
<img width="1062" alt="Screen Shot 2022-08-11 at 3 17 56 PM" src="https://user-images.githubusercontent.com/93849914/184221463-7cc7d27b-1eb6-4b9d-8b88-4fb7ba3db8bf.png">
<img width="1142" alt="Screen Shot 2022-08-11 at 3 18 20 PM" src="https://user-images.githubusercontent.com/93849914/184221536-1da8b725-d47b-4e79-89b8-d07b2c6e1d7d.png">
<img width="1120" alt="Screen Shot 2022-08-11 at 3 18 29 PM" src="https://user-images.githubusercontent.com/93849914/184221558-fb05a84a-6bbb-4322-ad23-3a73234796b8.png">
<img width="1122" alt="Screen Shot 2022-08-11 at 3 19 04 PM" src="https://user-images.githubusercontent.com/93849914/184221650-c09a0b99-eea0-4a13-9364-feebeb2b65d8.png">
<img width="1075" alt="Screen Shot 2022-08-11 at 3 19 10 PM" src="https://user-images.githubusercontent.com/93849914/184221663-3619c40b-5aa0-4d9b-bba2-1bb9a2c84edd.png">
<img width="1038" alt="Screen Shot 2022-08-11 at 3 19 20 PM" src="https://user-images.githubusercontent.com/93849914/184221692-7f1c5893-2242-4fef-b3b1-20078d6b3ac8.png">
<img width="1110" alt="Screen Shot 2022-08-11 at 3 19 31 PM" src="https://user-images.githubusercontent.com/93849914/184221720-facde610-2a7c-4511-ae87-244e68bd5ded.png">
<img width="1086" alt="Screen Shot 2022-08-11 at 3 19 40 PM" src="https://user-images.githubusercontent.com/93849914/184221744-637227bd-c027-4c36-81bd-a4ac7b7411a0.png">


