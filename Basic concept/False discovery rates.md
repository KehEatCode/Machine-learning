# FDR 错误发现率

<img width="283" alt="Screen Shot 2022-08-14 at 5 29 48 PM" src="https://user-images.githubusercontent.com/93849914/184555603-20341ece-bda7-47b5-963c-70f174136e4f.png">

- FDR are a tool to weed out bad data that looks good

    - can control the number of false positive by using 'Benjamini- Hochberg method'

         - To adjust p values in a way that limits the number of false positive that are reported as 'significant'
         - make p-value larger
             
             - For example, before the FDR correction, p-value might be 0.04(significant)
             - After FDR correlation, p-value might be 0.06(no longer significant)



- overlap, p value >0.05
- do not overlop, p value <0.05, this is called false positive, because the small p value suggest that the samples are from two types of mice (two seoarate distribution), and this is false
- false positive are rare

- 95% of the time the samples will overlap, p value >0.05
- 5% of the time the samples will not overlap, p value <0.05, results in a false positive

<img width="1138" alt="Screen Shot 2022-08-11 at 3 09 32 PM" src="https://user-images.githubusercontent.com/93849914/184220135-15fb0f78-3046-4d11-b1c2-8a833d9a1031.png">
