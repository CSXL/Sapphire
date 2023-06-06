import unittest
from typing import List, Tuple
from collections import Counter

from TokenSatisfaction.KeywordQualification import KeywordQualification
from RigorEvaluation.TFIDFEvaluation import TFIDFEvaluation
class test_keyword_qualification(unittest.TestCase):
    def test_keyword_qualification(self):
        ir_evaluator = TFIDFEvaluation("RBSUwFGa6Fk")

        # Perform text pre-processing
        ir_evaluator.lower_case_conversion()
        ir_evaluator.evaluate_term_freq()
        ir_evaluator.evaluate_inverse_doc_freq()
        ir_evaluator.initialize_json_scores()
        ir_evaluator.strip_non_ascii()
        ir_evaluator.filter_words()

        # Perform keyword qualification
        ir_evaluator.fallback_evaluation()
        k_qualifier = KeywordQualification(ir_evaluator.tokens, ir_evaluator.tf_idf_score)
        (freq_dist, qualification, qualified_terms) = k_qualifier.show()

        expected_freq_dist = {'let': 6, "'s": 16, 'talk': 2, 'about': 6, 'data': 31, 'science': 14, 'and': 40, 'some': 9, 'of': 19, 'the': 51, 'other': 2, 'related': 1, 'terms': 1, 'you': 12, 'may': 2, 'have': 18, 'heard': 1, 'such': 2, 'as': 2, 'predictive': 3, 'analytics': 7, 'machine': 4, 'learning': 4, 'advanced': 4, 'others': 1, 'so': 32, 'start': 6, 'with': 11, 'textbook': 1, 'definition': 1, 'is': 27, 'field': 1, 'study': 1, 'that': 31, 'involves': 4, 'extracting': 1, 'knowledge': 2, 'insights': 5, 'from': 1, 'noisy': 2, 'then': 9, 'turning': 1, 'those': 1, 'into': 6, 'actions': 2, 'our': 15, 'business': 11, 'or': 3, 'organization': 3, 'can': 15, 'take': 2, 'okay': 8, 'dig': 1, 'it': 16, 'a': 9, 'little': 1, 'bit': 1, 'more': 3, 'discuss': 1, 'what': 13, 'are': 5, 'different': 8, 'areas': 2, 'covered': 1, 'by': 4, 'really': 4, 'intersection': 2, 'between': 2, 'three': 3, 'disciplines': 2, 'we': 35, 'computer': 1, 'also': 5, 'cover': 1, 'area': 1, 'mathematics': 1, 'i': 6, 'think': 1, 'most': 1, 'important': 1, 'expertise': 4, 'these': 8, 'true': 1, 'initiatives': 1, 'involve': 1, 'collaboration': 2, 'across': 2, 'all': 1, 'now': 7, 'touch': 2, 'on': 7, 'types': 2, 'do': 9, 'need': 7, 'to': 25, 'understand': 1, 'here': 6, 'methods': 1, 'for': 7, 'questions': 7, 'might': 5, 'ask': 3, 'in': 15, 'an': 2, 'vary': 1, 'complexity': 2, 'value': 3, 'get': 2, 'out': 3, 'them': 2, 'chart': 1, 'first': 2, 'one': 2, 'descriptive': 1, 'this': 11, 'happening': 2, 'my': 1, 'right': 7, 'having': 2, 'accurate': 1, 'collection': 1, 'make': 4, 'sure': 3, 'know': 1, 'good': 1, 'question': 3, 'could': 2, 'well': 2, 'did': 3, 'sales': 4, 'go': 4, 'up': 2, 'down': 4, 'next': 6, 'level': 1, 'diagnostic': 1, 'why': 3, 'something': 1, 'happen': 2, 'drilling': 1, 'root': 1, 'cause': 1, 'problem': 1, 'likely': 1, 'will': 2, 'performance': 1, 'be': 2, 'quarter': 1, 'using': 2, 'historical': 1, 'patterns': 1, 'uh': 2, 'predict': 1, 'outcomes': 2, 'future': 3, 'finally': 1, 'prescriptive': 2, 'recommended': 1, 'best': 2, 'action': 2, 'particular': 1, 'outcome': 1, 'improve': 1, '10': 1, 'how': 2, 'done': 4, 'who': 2, 'actually': 3, 'does': 2, 'look': 1, 'at': 1, 'life': 3, 'cycle': 3, 'thing': 1, 'always': 1, 'must': 3, 'understanding': 2, 'critical': 3, "'re": 3, 'asking': 2, 'before': 2, 'lengthy': 1, 'initiative': 1, 'where': 1, 'see': 4, 'domain': 2, 'incredibly': 1, 'once': 5, "'ve": 4, 'defined': 1, 'move': 4, 'mining': 1, 'process': 2, 'going': 1, 'landscape': 1, 'procuring': 1, 'analysis': 3, 'cleaning': 2, 'reality': 1, 'marketplace': 2, 'when': 1, 'find': 3, 'probably': 2, 'not': 1, 'format': 1, 'has': 1, 'issues': 1, 'rows': 1, 'missing': 1, 'values': 1, 'duplicates': 1, 'there': 4, 'preparation': 1, 'ready': 1, 'cleansing': 1, 'exploration': 5, 'part': 1, 'allows': 1, 'us': 7, 'use': 1, 'analytical': 2, 'tools': 3, 'helping': 1, 'answer': 1, 'mentioned': 1, 'earlier': 1, 'if': 3, 'want': 3, 'higher': 1, 'like': 5, 'leverage': 1, 'massive': 2, 'amounts': 2, 'computing': 1, 'power': 1, 'high': 1, 'quality': 1, 'predictions': 1, 'prescribe': 1, 'perhaps': 1, 'visualize': 1, 'quickly': 1, 'roles': 4, 'analyst': 1, 'engineers': 1, 'scientists': 3, 'analysts': 2, 'obviously': 1, 'involved': 2, 'formulating': 1, 'they': 6, 'help': 7, 'but': 1, 'visualizing': 1, 'way': 1, 'useful': 1, 'folks': 2, 'engineering': 1, 'people': 2, 'clean': 1, "'ll": 2, 'techniques': 1, 'assist': 1, 'visualization': 1, 'overlap': 2, 'seeing': 1, 'nowadays': 1, 'sometimes': 2, 'their': 1, 'own': 1, 'lot': 1, 'collaborate': 1, 'each': 1, 'hope': 1, 'turn': 2, 'meaningful': 1, 'thank': 1, 'please': 2, 'drop': 1, 'line': 1, 'below': 1, 'videos': 1, 'subscribe': 1}
        expected_qualification = 41
        expected_qualified_terms = {'data': 6.377196998473731, 'science': 2.880024450923621, 'business': 2.26287635429713, 'okay': 1.6457282576706402, 'different': 1.6457282576706402, 'help': 1.4400122254618104, 'analytics': 1.4400122254618104, 'need': 1.4400122254618104, 'questions': 1.4400122254618104, 'right': 1.4400122254618104, 'start': 1.2342961932529801, 'let': 1.2342961932529801, 'insights': 1.02858016104415, 'exploration': 1.02858016104415, 'like': 1.02858016104415, 'really': 0.8228641288353201, 'roles': 0.8228641288353201, 'make': 0.8228641288353201, 'machine': 0.8228641288353201, 'learning': 0.8228641288353201, 'advanced': 0.8228641288353201, 've': 0.8228641288353201, 'sales': 0.8228641288353201, 'expertise': 0.8228641288353201, 'involves': 0.8228641288353201, 'future': 0.6171480966264901, 'cycle': 0.6171480966264901, 'question': 0.6171480966264901, 'critical': 0.6171480966264901, 'scientists': 0.6171480966264901, 'predictive': 0.6171480966264901, 'organization': 0.6171480966264901, 'analysis': 0.6171480966264901, 'ask': 0.6171480966264901, 'did': 0.6171480966264901, 'tools': 0.6171480966264901, 'want': 0.6171480966264901, 'life': 0.6171480966264901, 'actually': 0.6171480966264901, 'sure': 0.6171480966264901, 'value': 0.6171480966264901}
        self.assertEqual(freq_dist, expected_freq_dist)
        self.assertEqual(qualification, expected_qualification)
        self.assertEqual(qualified_terms, expected_qualified_terms)


if __name__ == '__main__':
    unittest.main()
