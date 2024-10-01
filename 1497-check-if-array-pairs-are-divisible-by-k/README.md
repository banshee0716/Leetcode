<h2><a href="https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/">1497. Check If Array Pairs Are Divisible by k</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36" data-immersive-translate-paragraph="1">Given an array of integers <code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">arr</code> of even length <code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">n</code> and an integer <code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">k</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個偶數長度<code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">n</code>的整數<code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">arr</code>和一個整數<code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">k</code>的陣列。</font></font></font></p>

<p data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36" data-immersive-translate-paragraph="1">We want to divide the array into exactly <code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">n / 2</code> pairs such that the sum of each pair is divisible by <code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">k</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">我們希望將陣列精確地分成<code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">n / 2</code>對，使得每對的總和可以被<code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">k</code>整除。</font></font></font></p>

<p data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36" data-immersive-translate-paragraph="1">Return <code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">true</code><em data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36"> If you can find a way to do that or </em><code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">false</code><em data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36"> otherwise</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><em data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">如果您能找到一種方法，則</em>傳回<code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">true</code> ，<em data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">否則</em>傳回<code data-immersive-translate-walked="27d7ff81-9848-40a5-a02c-4a44ebde0d36">false</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [1,2,3,4,5,10,6,7,8,9], k = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [1,2,3,4,5,6], k = 7
<strong>Output:</strong> true
<strong>Explanation:</strong> Pairs are (1,6),(2,5) and(3,4).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> arr = [1,2,3,4,5,6], k = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>arr.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> is even.</li>
	<li><code>-10<sup>9</sup> &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>
</div>