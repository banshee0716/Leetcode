<h2><a href="https://leetcode.com/problems/rank-transform-of-an-array/">1331. Rank Transform of an Array<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">1331. 陣列的秩變換</font></font></font></a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-walked="de49a778-2ebf-4a11-aa4a-5590f4084f69" data-immersive-translate-paragraph="1">Given an array of integers&nbsp;<code data-immersive-translate-walked="de49a778-2ebf-4a11-aa4a-5590f4084f69">arr</code>, replace each element with its rank.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數數組<code data-immersive-translate-walked="de49a778-2ebf-4a11-aa4a-5590f4084f69">arr</code> ，將每個元素替換為其排名。</font></font></font></p>

<p data-immersive-translate-walked="de49a778-2ebf-4a11-aa4a-5590f4084f69" data-immersive-translate-paragraph="1">The rank represents how large the element is. The rank has the following rules:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">等級代表元素的大小。排名有以下規則：</font></font></font></p>

<ul>
	<li data-immersive-translate-walked="de49a778-2ebf-4a11-aa4a-5590f4084f69" data-immersive-translate-paragraph="1">Rank is an integer starting from 1.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">Rank 是從 1 開始的整數。</font></font></font></li>
	<li data-immersive-translate-walked="de49a778-2ebf-4a11-aa4a-5590f4084f69" data-immersive-translate-paragraph="1">The larger the element, the larger the rank. If two elements are equal, their rank must be the same.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">元素越大，等級越大。如果兩個元素相等，則它們的秩必須相同。</font></font></font></li>
	<li data-immersive-translate-walked="de49a778-2ebf-4a11-aa4a-5590f4084f69" data-immersive-translate-paragraph="1">Rank should be as small as possible.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">排名應該盡可能小。</font></font></font></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [40,10,20,30]
<strong>Output:</strong> [4,1,2,3]
<strong>Explanation</strong>: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [100,100,100]
<strong>Output:</strong> [1,1,1]
<strong>Explanation</strong>: Same elements share the same rank.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> arr = [37,12,28,9,100,56,80,5,12]
<strong>Output:</strong> [5,3,4,2,8,6,7,1,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>