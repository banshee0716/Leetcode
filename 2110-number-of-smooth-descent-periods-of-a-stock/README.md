<h2><a href="https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/">2110. Number of Smooth Descent Periods of a Stock</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">You are given an integer array <code data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">prices</code> representing the daily price history of a stock, where <code data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">prices[i]</code> is the stock price on the <code data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">i<sup>th</sup></code> day.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您將獲得一個整數陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">prices</code> ，代表股票的每日價格歷史，其中 <code data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">prices[i]</code> 當天的股票價格 <code data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">i<sup>th</sup></code> 。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">A <strong data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">smooth descent period</strong> of a stock consists of <strong data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">one or more contiguous</strong> days such that the price on each day is <strong data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">lower</strong> than the price on the <strong data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">preceding day</strong> by <strong data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">exactly</strong> <code data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">1</code>. The first day of the period is exempted from this rule.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">股票的平滑下降期由一個或多個連續的日子組成，使得每天的價格正好 <code data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">1</code> 低於前一天的價格。期間的第一天不受此規則的約束。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">Return <em data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">the number of <strong data-immersive-translate-effect="1" data-immersive_translate_walked="31f89ce1-0843-46c8-b1a5-d679f40ecbf8">smooth descent periods</strong></em>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回平滑下降週期數。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> prices = [3,2,1,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> prices = [8,6,7,7]
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> prices = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is 1 smooth descent period: [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>