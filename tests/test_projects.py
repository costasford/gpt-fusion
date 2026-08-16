from gpt_fusion.projects import PROJECTS, Project


def test_projects_is_nonempty_list_of_project():
    assert len(PROJECTS) > 0
    assert all(isinstance(p, Project) for p in PROJECTS)


def test_project_ids_are_unique():
    ids = [p.id for p in PROJECTS]
    assert len(ids) == len(set(ids))


def test_each_project_has_nonempty_fields():
    for project in PROJECTS:
        assert project.id.strip()
        assert project.name.strip()
        assert project.description.strip()


def test_known_project_ids_present():
    ids = {p.id for p in PROJECTS}
    assert {
        "python-utilities",
        "auth-ui-kit",
        "unity-prototype",
        "top-viewer-games",
        "tutorial",
    } <= ids
