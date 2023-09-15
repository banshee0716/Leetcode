<h2><a href="https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/">1608. Special Array With X Elements Greater Than or Equal X</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">You are given an array <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code> of non-negative integers. <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code> is considered <strong data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">special</strong> if there exists a number <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> such that there are <strong data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">exactly</strong> <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> numbers in <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code> that are <strong data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">greater than or equal to</strong> <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您將獲得一個非負整數陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code> 。 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code> 如果存在一個數位 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> ，使得其中正 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code> 好 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> 存在大於或等於的數位，則認為是特殊的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> 。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">Notice that <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> <strong data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">does not</strong> have to be an element in <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">請注意，不必 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> 是 中的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code> 元素。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">Return <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> <em data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">if the array is <strong data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">special</strong>, otherwise, return </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">-1</code>. It can be proven that if <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code> is special, the value for <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> is <strong data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">unique</strong>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果陣列是特殊的，則傳回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> ，否則傳回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">-1</code> 。可以證明，如果特殊，則 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">nums</code> 的值 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f2b59c21-a4c7-4a58-9710-be6c4c7b6edf">x</code> 是唯一的。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 values (3 and 5) that are greater than or equal to 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,0]
<strong>Output:</strong> -1
<strong>Explanation:</strong> No numbers fit the criteria for x.
If x = 0, there should be 0 numbers &gt;= x, but there are 2.
If x = 1, there should be 1 number &gt;= x, but there are 0.
If x = 2, there should be 2 numbers &gt;= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [0,4,3,0,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 values that are greater than or equal to 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
</div>