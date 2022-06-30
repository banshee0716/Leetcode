double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
 int m, n;
    for (int i=0,j=0,k=0;i< (nums1Size+nums2Size) / 2 + 1;i++){ //求中位數，ｊｋ是類似雙指針的概念
        if (j >= nums1Size)
            m = nums2[k++];
        else if (k >= nums2Size)
            m = nums1[j++];
        else
            m = nums1[j] < nums2[k] ? nums1[j++] : nums2[k++];
        if (i == (nums1Size+nums2Size-1)/2)
            n=m;
    }
    return (n+m)/2.0f;
}
