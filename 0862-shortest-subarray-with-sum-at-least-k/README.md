<h2><a href="https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/">862. Shortest Subarray with Sum at Least K</a></h2><h3>Hard</h3><hr><div><p data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04" data-immersive-translate-paragraph="1">Given an integer array <code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">nums</code> and an integer <code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">k</code>, return <em data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">the length of the shortest non-empty <strong data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">subarray</strong> of </em><code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">nums</code><em data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04"> with a sum of at least </em><code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">k</code>. If there is no such <strong data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">subarray</strong>, return <code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">-1</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數數組<code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">nums</code>和一個整數<code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">k</code> ，傳回<em data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">總和至少為</em><code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">k</code>的<code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">nums</code><em data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">的最短非空子<strong data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">數組</strong>的長度</em>。如果不存在這樣的<strong data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">子數組</strong>，則傳回<code data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">-1</code> 。</font></font></font></p>

<p data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04" data-immersive-translate-paragraph="1">A <strong data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">subarray</strong> is a <strong data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">contiguous</strong> part of an array.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">子數組</strong>是數組的<strong data-immersive-translate-walked="2b472700-65b9-4b16-baee-ee8d4ebdfb04">連續</strong>部分。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> 1
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2], k = 4
<strong>Output:</strong> -1
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [2,-1,2], k = 3
<strong>Output:</strong> 3
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
</div>