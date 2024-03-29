<h2><a href="https://leetcode.com/problems/minimum-processing-time/">2895. Minimum Processing Time</a></h2><h3>Medium</h3><hr><div><p>You have <code>n</code> processors each having <code>4</code> cores and <code>n * 4</code> tasks that need to be executed such that each core should perform only <strong>one</strong> task.</p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="d5f94fdd-f705-4d7a-8bbf-1b517fe68c78">Given a <strong data-immersive-translate-effect="1" data-immersive_translate_walked="d5f94fdd-f705-4d7a-8bbf-1b517fe68c78">0-indexed</strong> integer array <code data-immersive-translate-effect="1" data-immersive_translate_walked="d5f94fdd-f705-4d7a-8bbf-1b517fe68c78">processorTime</code> representing the time at which each processor becomes available for the first time and a <strong data-immersive-translate-effect="1" data-immersive_translate_walked="d5f94fdd-f705-4d7a-8bbf-1b517fe68c78">0-indexed </strong>integer array <code data-immersive-translate-effect="1" data-immersive_translate_walked="d5f94fdd-f705-4d7a-8bbf-1b517fe68c78">tasks</code> representing the time it takes to execute each task, return <em data-immersive-translate-effect="1" data-immersive_translate_walked="d5f94fdd-f705-4d7a-8bbf-1b517fe68c78">the <strong data-immersive-translate-effect="1" data-immersive_translate_walked="d5f94fdd-f705-4d7a-8bbf-1b517fe68c78">minimum</strong> time when all of the tasks have been executed by the processors.</em><font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個表示每個處理器首次可用的時間的 0 索引整數數位列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="d5f94fdd-f705-4d7a-8bbf-1b517fe68c78">processorTime</code> 和一個表示執行每個任務所需時間的 0 索引整數數位 <code data-immersive-translate-effect="1" data-immersive_translate_walked="d5f94fdd-f705-4d7a-8bbf-1b517fe68c78">tasks</code> ，傳回處理器執行所有任務時的最短時間。</font></font></font></p>

<p><strong>Note: </strong>Each core executes the task independently of the others.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]
<strong>Output:</strong> 16
<strong>Explanation:</strong> 
It's optimal to assign the tasks at indexes 4, 5, 6, 7 to the first processor which becomes available at time = 8, and the tasks at indexes 0, 1, 2, 3 to the second processor which becomes available at time = 10. 
Time taken by the first processor to finish execution of all tasks = max(8 + 8, 8 + 7, 8 + 4, 8 + 5) = 16.
Time taken by the second processor to finish execution of all tasks = max(10 + 2, 10 + 2, 10 + 3, 10 + 1) = 13.
Hence, it can be shown that the minimum time taken to execute all the tasks is 16.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]
<strong>Output:</strong> 23
<strong>Explanation:</strong> 
It's optimal to assign the tasks at indexes 1, 4, 5, 6 to the first processor which becomes available at time = 10, and the tasks at indexes 0, 2, 3, 7 to the second processor which becomes available at time = 20.
Time taken by the first processor to finish execution of all tasks = max(10 + 3, 10 + 5, 10 + 8, 10 + 4) = 18.
Time taken by the second processor to finish execution of all tasks = max(20 + 2, 20 + 1, 20 + 2, 20 + 3) = 23.
Hence, it can be shown that the minimum time taken to execute all the tasks is 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == processorTime.length &lt;= 25000</code></li>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= processorTime[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= tasks[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>tasks.length == 4 * n</code></li>
</ul>
</div>