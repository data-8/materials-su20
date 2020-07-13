test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure reasonable_test_statistics is an array!;
          >>> type(reasonable_test_statistics) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(reasonable_test_statistics) > 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Total variation distance wouldn't work with the alternative hypothesis. ;
          >>> # TVD takes the absolute value, so it does not care about direction.;
          >>> # However, the alternative hypothesis implies that we do care about direction; it states that there is a *higher* chance of getting a spam call with area code 781.;
          >>> # Using TVD as a statistic would not help us in determining if there is a higher chance. ;
          >>> np.any(reasonable_test_statistics == 2)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The probability of getting 781 out of all possible area codes is 1/800. Probability is a fixed number, so it would not make sense to use it as a statistic. ;
          >>> np.any(reasonable_test_statistics == 3)
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
