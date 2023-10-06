<h2><a href="https://leetcode.com/problems/most-frequent-even-element/">2404. Most Frequent Even Element</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="8e511945-5ec5-4f4e-9960-f10c8b94e2da">Given an integer array <code data-immersive-translate-effect="1" data-immersive_translate_walked="8e511945-5ec5-4f4e-9960-f10c8b94e2da">nums</code>, return <em data-immersive-translate-effect="1" data-immersive_translate_walked="8e511945-5ec5-4f4e-9960-f10c8b94e2da">the most frequent even element</em>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="8e511945-5ec5-4f4e-9960-f10c8b94e2da">nums</code> ，返回最頻繁的偶數元素。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="8e511945-5ec5-4f4e-9960-f10c8b94e2da">If there is a tie, return the <strong data-immersive-translate-effect="1" data-immersive_translate_walked="8e511945-5ec5-4f4e-9960-f10c8b94e2da">smallest</strong> one. If there is no such element, return <code data-immersive-translate-effect="1" data-immersive_translate_walked="8e511945-5ec5-4f4e-9960-f10c8b94e2da">-1</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果存在平局，則返回最小的平局。如果沒有這樣的元素，則傳回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="8e511945-5ec5-4f4e-9960-f10c8b94e2da">-1</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,2,2,4,4,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [4,4,4,9,2,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong> 4 is the even element appears the most.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [29,47,21,41,13,37,25,7]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no even element.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>