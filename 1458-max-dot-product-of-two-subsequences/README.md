<h2><a href="https://leetcode.com/problems/max-dot-product-of-two-subsequences/">1458. Max Dot Product of Two Subsequences</a></h2><h3>Hard</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">Given two arrays <code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">nums1</code>&nbsp;and <code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114"><font face="monospace">nums2</font></code><font face="monospace" data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">.</font><font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定兩個陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">nums1</code> 和 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114"><font face="monospace">nums2</font></code> .</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">Return the maximum dot product&nbsp;between&nbsp;<strong data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">non-empty</strong> subsequences of nums1 and nums2 with the same length.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回長度相同的 nums1 和 nums2 的非空子序列之間的最大點積。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie,&nbsp;<code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">[2,3,5]</code>&nbsp;is a subsequence of&nbsp;<code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">[1,2,3,4,5]</code>&nbsp;while <code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">[1,5,3]</code>&nbsp;is not).<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">陣列的子序列是一個新陣列，它通過刪除一些（可以是無）字元而不干擾其餘字元的相對位置而從原始數位形成。（即， <code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">[2,3,5]</code> 是 while <code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">[1,5,3]</code> 不是的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5d958118-a308-4bd0-b981-bcc0e08e3114">[1,2,3,4,5]</code> 子序列）。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums1 = [2,1,-2,5], nums2 = [3,0,-6]
<strong>Output:</strong> 18
<strong>Explanation:</strong> Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums1 = [3,-2], nums2 = [2,-6,7]
<strong>Output:</strong> 21
<strong>Explanation:</strong> Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums1 = [-1,-1], nums2 = [1,1]
<strong>Output:</strong> -1
<strong>Explanation: </strong>Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 500</code></li>
	<li><code>-1000 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>
</div>