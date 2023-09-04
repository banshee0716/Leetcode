<h2><a href="https://leetcode.com/problems/subarray-sums-divisible-by-k/">974. Subarray Sums Divisible by K</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">Given an integer array <code data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">nums</code> and an integer <code data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">k</code>, return <em data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">the number of non-empty <strong data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">subarrays</strong> that have a sum divisible by </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">k</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數陣列和一個整數 <code data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">k</code> ，返回總和可被 整除的非空子陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">nums</code> 的數目 <code data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">k</code> 。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">A <strong data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">subarray</strong> is a <strong data-immersive-translate-effect="1" data-immersive_translate_walked="001012c8-ba8c-464f-bf8a-5bbce3e7842d">contiguous</strong> part of an array.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">子陣列是陣列的連續部分。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [4,5,0,-2,-3,1], k = 5
<strong>Output:</strong> 7
<strong>Explanation:</strong> There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [5], k = 9
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>2 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>
</div>