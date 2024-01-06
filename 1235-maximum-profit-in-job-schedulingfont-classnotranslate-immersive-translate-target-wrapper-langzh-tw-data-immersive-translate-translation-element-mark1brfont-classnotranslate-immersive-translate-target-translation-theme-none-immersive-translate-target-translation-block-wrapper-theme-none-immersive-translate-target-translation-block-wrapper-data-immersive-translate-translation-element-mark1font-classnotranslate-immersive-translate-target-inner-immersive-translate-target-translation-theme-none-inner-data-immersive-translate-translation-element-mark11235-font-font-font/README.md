<h2><a href="https://leetcode.com/problems/maximum-profit-in-job-scheduling/">1235. Maximum Profit in Job Scheduling<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">1235. 作業調度的最大利潤</font></font></font></a></h2><h3>Hard</h3><hr><div><p data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3" data-immersive-translate-paragraph="1">We have <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">n</code> jobs, where every job is scheduled to be done from <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">startTime[i]</code> to <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">endTime[i]</code>, obtaining a profit of <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">profit[i]</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">我們有工作，其中每項 <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">n</code> 工作都計劃從 <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">startTime[i]</code> 到 <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">endTime[i]</code> 完成，獲得的利潤 <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">profit[i]</code> 。</font></font></font></p>

<p data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3" data-immersive-translate-paragraph="1">You're given the <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">startTime</code>, <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">endTime</code> and <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">profit</code> arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定 <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">startTime</code> 和 <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">endTime</code> <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">profit</code> 陣列，返回您可以獲得的最大利潤，這樣子集中沒有兩個具有重疊時間範圍的工作。</font></font></font></p>

<p data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3" data-immersive-translate-paragraph="1">If you choose a job that ends at time <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">X</code> you will be able to start another job that starts at time <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">X</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果選擇在時間結束的作業，您將能夠開始另一個在時間 <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">X</code> <code data-immersive-translate-walked="f41ef102-97b4-46de-9bed-0ea54bb7cfc3">X</code> 開始的作業。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png" style="width: 380px; height: 154px;"></strong></p>

<pre><strong>Input:</strong> startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
<strong>Output:</strong> 120
<strong>Explanation:</strong> The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/10/sample22_1584.png" style="width: 600px; height: 112px;"> </strong></p>

<pre><strong>Input:</strong> startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
<strong>Output:</strong> 150
<strong>Explanation:</strong> The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/10/sample3_1584.png" style="width: 400px; height: 112px;"></strong></p>

<pre><strong>Input:</strong> startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= startTime.length == endTime.length == profit.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= startTime[i] &lt; endTime[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= profit[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>