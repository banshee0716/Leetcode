<h2><a href="https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/">1481. Least Number of Unique Integers after K Removals</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="8b704ed7-d117-4533-b360-af2c6c3c3a0d" data-immersive-translate-paragraph="1">Given an array of integers&nbsp;<code data-immersive-translate-walked="8b704ed7-d117-4533-b360-af2c6c3c3a0d">arr</code>&nbsp;and an integer <code data-immersive-translate-walked="8b704ed7-d117-4533-b360-af2c6c3c3a0d">k</code>.&nbsp;Find the <em data-immersive-translate-walked="8b704ed7-d117-4533-b360-af2c6c3c3a0d">least number of unique integers</em>&nbsp;after removing <strong data-immersive-translate-walked="8b704ed7-d117-4533-b360-af2c6c3c3a0d">exactly</strong> <code data-immersive-translate-walked="8b704ed7-d117-4533-b360-af2c6c3c3a0d">k</code> elements<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數陣列和一個整數 <code data-immersive-translate-walked="8b704ed7-d117-4533-b360-af2c6c3c3a0d">arr</code> <code data-immersive-translate-walked="8b704ed7-d117-4533-b360-af2c6c3c3a0d">k</code> 。精確刪除 <code data-immersive-translate-walked="8b704ed7-d117-4533-b360-af2c6c3c3a0d">k</code> 元素后找到最少數量的唯一整數</font></font></font><b>.</b></p>

<ol>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input: </strong>arr = [5,5,4], k = 1
<strong>Output: </strong>1
<strong>Explanation</strong>: Remove the single 4, only 5 is left.
</pre>
<strong class="example">Example 2:</strong>

<pre><strong>Input: </strong>arr = [4,3,1,1,3,3,2], k = 3
<strong>Output: </strong>2
<strong>Explanation</strong>: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 10^5</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10^9</code></li>
	<li><code>0 &lt;= k&nbsp;&lt;= arr.length</code></li>
</ul></div>