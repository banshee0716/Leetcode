<h2><a href="https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/">2044. Count Number of Maximum Bitwise-OR Subsets<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">2044. 計算最大位元或子集的數量</font></font></font></a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e" data-immersive-translate-paragraph="1">Given an integer array <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">nums</code>, find the <strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">maximum</strong> possible <strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">bitwise OR</strong> of a subset of <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">nums</code> and return <em data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">the <strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">number of different non-empty subsets</strong> with the maximum bitwise OR</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數數組<code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">nums</code> ，找到<code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">nums</code>子集的<strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">最大</strong>可能<strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">按位 OR</strong> ，並傳回<em data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">具有最大按位 OR 的<strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">不同非空子集的數量</strong></em>。</font></font></font></p>

<p data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e" data-immersive-translate-paragraph="1">An array <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">a</code> is a <strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">subset</strong> of an array <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">b</code> if <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">a</code> can be obtained from <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">b</code> by deleting some (possibly zero) elements of <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">b</code>. Two subsets are considered <strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">different</strong> if the indices of the elements chosen are different.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果可以透過刪除<code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">b</code>的一些（可能為零）元素從<code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">b</code>獲得<code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">a</code> ，則數組<code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">a</code>是數組<code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">b</code>的<strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">子集</strong>。如果所選元素的索引不同，則認為兩個子集<strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">不同</strong>。</font></font></font></p>

<p data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e" data-immersive-translate-paragraph="1">The bitwise OR of an array <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">a</code> is equal to <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">a[0] <strong>OR</strong> a[1] <strong>OR</strong> ... <strong>OR</strong> a[a.length - 1]</code> (<strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">0-indexed</strong>).<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">數組<code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">a</code>的位或等於 <code data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">a[0] <strong>OR</strong> a[1] <strong>OR</strong> ... <strong>OR</strong> a[a.length - 1]</code> （ <strong data-immersive-translate-walked="380c8cf4-5ad3-452e-bb97-5611a620544e">0-索引</strong>）。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,2,2]
<strong>Output:</strong> 7
<strong>Explanation:</strong> All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 2<sup>3</sup> - 1 = 7 total subsets.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,1,5]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 16</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>