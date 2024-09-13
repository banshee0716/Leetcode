<h2><a href="https://leetcode.com/problems/xor-queries-of-a-subarray/">1310. XOR Queries of a Subarray</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8" data-immersive-translate-paragraph="1">You are given an array <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">arr</code> of positive integers. You are also given the array <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">queries</code> where <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">queries[i] = [left<sub>i, </sub>right<sub>i</sub>]</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個正整數數組<code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">arr</code> 。您還會獲得數組<code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">queries</code> ，其中<code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">queries[i] = [left <sub>i,</sub> right <sub>i</sub> ]</code> 。</font></font></font></p>

<p data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8" data-immersive-translate-paragraph="1">For each query <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">i</code> compute the <strong data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">XOR</strong> of elements from <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">left<sub>i</sub></code> to <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">right<sub>i</sub></code> (that is, <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">arr[left<sub>i</sub>] XOR arr[left<sub>i</sub> + 1] XOR ... XOR arr[right<sub>i</sub>]</code> ).<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">對於每個查詢， <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">i</code>計算從左<code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8"><sub>left i</sub></code>到<code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">right <sub>i</sub></code>的元素的<strong data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">異或</strong>（即， <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">arr[left<sub>i</sub>] XOR arr[left<sub>i</sub> + 1] XOR ... XOR arr[right<sub>i</sub>]</code> ）。</font></font></font></p>

<p data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8" data-immersive-translate-paragraph="1">Return an array <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">answer</code> where <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">answer[i]</code> is the answer to the <code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">i<sup>th</sup></code> query.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回一個陣列<code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">answer</code> ，其中<code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">answer[i]</code>是<code data-immersive-translate-walked="bc4d80ec-cd29-48c0-bd96-4f347e63fbc8">i <sup>th</sup></code>查詢的答案。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
<strong>Output:</strong> [2,7,14,8] 
<strong>Explanation:</strong> 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
<strong>Output:</strong> [8,0,4,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length, queries.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= left<sub>i</sub> &lt;= right<sub>i</sub> &lt; arr.length</code></li>
</ul>
</div>