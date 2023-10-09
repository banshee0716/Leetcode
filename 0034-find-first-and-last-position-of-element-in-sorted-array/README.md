<h2><a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/">34. Find First and Last Position of Element in Sorted Array</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">Given an array of integers <code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">nums</code> sorted in non-decreasing order, find the starting and ending position of a given <code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">target</code> value.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個按非降序排序的整數陣列，找到給定 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">target</code> 值的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">nums</code> 起始和結束位置。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">If <code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">target</code> is not found in the array, return <code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">[-1, -1]</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果在陣列中找不到，則 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">target</code> 傳回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">[-1, -1]</code> 。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">You must&nbsp;write an algorithm with&nbsp;<code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">O(log n)</code> runtime complexity.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">必須編寫具有運行時複雜性的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b0f2c0ac-1cfb-4d91-80fc-9d93efeadb20">O(log n)</code> 演算法。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is a non-decreasing array.</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>
</div>