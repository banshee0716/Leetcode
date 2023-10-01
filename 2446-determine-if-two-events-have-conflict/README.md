<h2><a href="https://leetcode.com/problems/determine-if-two-events-have-conflict/">2446. Determine if Two Events Have Conflict</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">You are given two arrays of strings that represent two inclusive events that happened <strong data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">on the same day</strong>, <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">event1</code> and <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">event2</code>, where:<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您將取得兩個字串陣列，它們表示同一天發生的兩個包含事件，以及 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">event2</code> ， <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">event1</code> 其中：</font></font></font></p>

<ul>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da"><code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">event1 = [startTime<sub>1</sub>, endTime<sub>1</sub>]</code> and<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><font class="notranslate" data-immersive-translate-translation-element-mark="1">&nbsp;</font><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-inline-wrapper-theme-none immersive-translate-target-translation-inline-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">event1 = [startTime<sub>1</sub>, endTime<sub>1</sub>]</code> 和</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da"><code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">event2 = [startTime<sub>2</sub>, endTime<sub>2</sub>]</code>.</li>
</ul>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">Event times are valid 24 hours format in the form of <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">HH:MM</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">事件時間以 24 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">HH:MM</code> 小時格式有效，格式為 。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">A <strong data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">conflict</strong> happens when two events have some non-empty intersection (i.e., some moment is common to both events).<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">當兩個事件有一些非空的交集（即，兩個事件共有某個時刻）時，就會發生衝突。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">Return <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">true</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da"> if there is a conflict between two events. Otherwise, return </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">false</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果兩個事件之間存在衝突，則返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">true</code> 。否則，返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5dd2f617-b280-4fe6-8f89-75dbec52e4da">false</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
<strong>Output:</strong> true
<strong>Explanation:</strong> The two events intersect at time 2:00.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
<strong>Output:</strong> true
<strong>Explanation:</strong> The two events intersect starting from 01:20 to 02:00.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
<strong>Output:</strong> false
<strong>Explanation:</strong> The two events do not intersect.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>evnet1.length == event2.length == 2.</code></li>
	<li><code>event1[i].length == event2[i].length == 5</code></li>
	<li><code>startTime<sub>1</sub> &lt;= endTime<sub>1</sub></code></li>
	<li><code>startTime<sub>2</sub> &lt;= endTime<sub>2</sub></code></li>
	<li>All the event times follow the <code>HH:MM</code> format.</li>
</ul>
</div>