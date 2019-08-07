Feature: Check if a word or a phrase is an anagram of the subject word or phrase.

  Scenario Outline: Understand failure cases better
    When I ask if the word or phrase "<subject>" is an anagram of the word or phrase "<candidate>"
    Then I see a message - can not check for anagram because "<reason>"

    Examples: 
      | subject     | candidate   | reason                                         |
      | #@          | this phrase | Subject or Candidate is not valid String       |
      | that phrase | ~!          | Subject or Candidate is not valid String       |
      |             | that phrase | Subject or Candidate length does not match     |
      | this phrase |             | Subject or Candidate length does not match     |
      | ~!          | \\"         | Subject or Candidate is not valid String       |
      | \\'         | #@          | Subject or Candidate is not valid String       |

  Scenario Outline: Successfully identify anagrams and non-anagrams in both-directions
    When I ask if the word or phrase "<subject>" is an anagram of the word or phrase "<candidate>"
    Then I see a message "<candidate>" "<result>" an anagram of "<subject>"
    
    Examples: 
      | subject     | candidate  | result |
      | this phrase | earthships | is     |
      | word        | drow       | is     |
      | word        | drom       | is not |
      | gut         | tug        | is     |
