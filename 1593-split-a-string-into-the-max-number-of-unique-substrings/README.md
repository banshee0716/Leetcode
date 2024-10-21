<h2><a href="https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/">1593. Split a String Into the Max Number of Unique Substrings</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="a9b7393d-c874-4cbb-9199-24e1d7603593" data-immersive-translate-paragraph="1">Given a string&nbsp;<code data-immersive-translate-walked="a9b7393d-c874-4cbb-9199-24e1d7603593">s</code><var>,</var>&nbsp;return <em data-immersive-translate-walked="a9b7393d-c874-4cbb-9199-24e1d7603593">the maximum&nbsp;number of unique substrings that the given string can be split into</em>.</p>

<p data-immersive-translate-walked="a9b7393d-c874-4cbb-9199-24e1d7603593" data-immersive-translate-paragraph="1">You can split string&nbsp;<code data-immersive-translate-walked="a9b7393d-c874-4cbb-9199-24e1d7603593">s</code> into any list of&nbsp;<strong data-immersive-translate-walked="a9b7393d-c874-4cbb-9199-24e1d7603593">non-empty substrings</strong>, where the concatenation of the substrings forms the original string.&nbsp;However, you must split the substrings such that all of them are <strong data-immersive-translate-walked="a9b7393d-c874-4cbb-9199-24e1d7603593">unique</strong>.</p>

<p data-immersive-translate-walked="a9b7393d-c874-4cbb-9199-24e1d7603593" data-immersive-translate-paragraph="1">A <strong data-immersive-translate-walked="a9b7393d-c874-4cbb-9199-24e1d7603593">substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "ababccc"
<strong>Output:</strong> 5
<strong>Explanation</strong>: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "aba"
<strong>Output:</strong> 2
<strong>Explanation</strong>: One way to split maximally is ['a', 'ba'].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "aa"
<strong>Output:</strong> 1
<strong>Explanation</strong>: It is impossible to split the string any further.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>
	<p><code>1 &lt;= s.length&nbsp;&lt;= 16</code></p>
	</li>
	<li>
	<p><code>s</code> contains&nbsp;only lower case English letters.</p>
	</li>
</ul>
</div>