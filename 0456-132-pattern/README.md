<h2><a href="https://leetcode.com/problems/132-pattern/">456. 132 Pattern</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">Given an array of <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">n</code> integers <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums</code>, a <strong data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">132 pattern</strong> is a subsequence of three integers <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums[i]</code>, <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums[j]</code> and <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums[k]</code> such that <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">i &lt; j &lt; k</code> and <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums[i] &lt; nums[k] &lt; nums[j]</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數陣列，一個 132 模式是三個 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">n</code> 整數的子序列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums</code> <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums[i]</code> ， <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums[j]</code> 使得 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums[k]</code> <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">i &lt; j &lt; k</code> 和 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums[i] &lt; nums[k] &lt; nums[j]</code> 。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">Return <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">true</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630"> if there is a <strong data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">132 pattern</strong> in </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">, otherwise, return </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">false</code><font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果中有 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">nums</code> 132 模式，則返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">true</code> ，否則返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49ced7e9-6485-4d28-8012-77db84b19630">false</code> </font></font></font><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no 132 pattern in the sequence.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,4,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a 132 pattern in the sequence: [1, 4, 2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [-1,3,2,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>