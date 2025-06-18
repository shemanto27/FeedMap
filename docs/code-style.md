# Code Style Guide for FeedMap Backend

## Project Structure
We follow a **modular feature-based structure**, where each application (e.g., users, roadmap, interactions- comments, reply, upvote) is a separate Django app. This promotes separation of concerns and makes it easier to reuse.

## API Design
- Follows **RESTful principles**
- URL patterns are resource-oriented: `/api/roadmap/`, `/api/comments/`
- Only authenticated users can interact with roadmap items.

## Naming Conventions
- **Apps** use lowercase, underscores(_app) at the end, plural: `users_app`, `roadmaps_app`, `interactions_app`
- **Models** use singular PascalCase: `RoadmapItem`, `Comment`
- **Views** use class-based views with `DRF` generics
- **Serializers** named `<ModelName>Serializer`

## Patterns Used
- Django REST Framework (DRF) for APIs
- Permissions handled via `permissions.py`
- Clean separation of serializers, views, and models

## Benefits
- Easy to maintain as codebase grows
- Promotes reusability
- Improves readability for reviewers or teammates
