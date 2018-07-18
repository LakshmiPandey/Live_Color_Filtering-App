# Live_Color_Filtering-App
This application filter only some specific color in the real time. (Open CV)


___________________________________________________________________________________________

* This application filter the real time color from the given frame.
* You can use the same script for filtering various color as the same time or different.
* For different colors , do refer the FilteringChart.png in the repository.
* By changin the upper bound and the lower bound , you can easily achive .

____________________________________________________________________________________________

Various steps taken are:
1) Initialising the color bound you want to filter.
2) Converting the image to HSV.
3) Masking the image to that color bound you want to filter.
4) Bitwise anding the original frame to get the required result.

_____________________________________________________________________________________________


